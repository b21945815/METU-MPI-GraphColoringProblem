#include <mpi.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <set> 
#include <numeric>
#include <iomanip>
#include "graph.h"         
#include "algorithm2-basic.h"    
#include <fstream>

using namespace std;
using namespace Algorithm2Basic;

void Algorithm2Basic::parallelGreedyColoring(vector<vector<int>>& graph, int rank, int size, vector<int>& colors) {
    int n = graph.size();
    int blockSize = n / size;

    int start = rank * blockSize;
    int end = (rank == size - 1) ? n : (rank + 1) * blockSize;

    vector<int> localColors(n, -1);
    vector<bool> available(n, true);

    for (int u = start; u < end; ++u) {
        fill(available.begin(), available.end(), true);

        for (int v : graph[u]) {
            if (localColors[v] != -1) {
                available[localColors[v]] = false;
            }
        }
        for (int color = 0; color < n; ++color) {
            if (available[color]) {
                localColors[u] = color;
                // cout << "Rank " << rank << " assigned color " << color << " to vertex " << u << endl;
                break;
            }
        }
        MPI_Gather(localColors.data() + start, blockSize, MPI_INT, colors.data(), blockSize, MPI_INT, 0, MPI_COMM_WORLD);
        MPI_Bcast(colors.data(), n, MPI_INT, 0, MPI_COMM_WORLD);
    }

}

void Algorithm2Basic::recolorWithReverseOrdering(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, int colNum) {
    int n = graph.size();

    for (int k = colNum - 1; k >= 0; --k) {
        vector<int> colorClass(n, -1);
        int index = 0;
        for (int i = 0; i < n; ++i) {
            if (colors[i] == k) {
                colorClass[index++] = i;
            }
        }

        int blockSize = n / size;
        int start = rank * blockSize;
        int end = (rank == size - 1) ? n : (rank + 1) * blockSize;

        vector<int> localColors = colors;
        for (int idx = start; idx < end; ++idx) {
            int vertex = colorClass[idx];
            if (vertex == -1) continue;

            vector<bool> available(colNum, true);

            for (int neighbor : graph[vertex]) {
                if (localColors[neighbor] != -1) {
                    available[localColors[neighbor]] = false;
                }
            }

            for (int newColor = 0; newColor < colNum; ++newColor) {
                if (available[newColor]) {
                    localColors[vertex] = newColor;
                    // cout << "Rank " << rank << " assigned color " << newColor << " to vertex " << vertex << endl;
                    break;
                }
            }
        }

        MPI_Gather(localColors.data() + rank * blockSize, blockSize, MPI_INT,
            colors.data(), blockSize, MPI_INT, 0, MPI_COMM_WORLD);

        MPI_Bcast(colors.data(), n, MPI_INT, 0, MPI_COMM_WORLD);

    }

}

void Algorithm2Basic::detectConflicts(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& allConflicts) {
    int n = graph.size();
    int blockSize = n / size;

    int start = rank * blockSize;
    int end = (rank == size - 1) ? n : (rank + 1) * blockSize;

    vector<int> localConflicts;
    int check = 0;
    for (int u = start; u < end; ++u) {
        check = 0;
        for (int v : graph[u]) {
            if (colors[u] == colors[v]) {
                if (u < v) {
                    localConflicts.push_back(u);
                    check = 1;
                    break;
                }
            }
        }
        if (check == 0) {
            localConflicts.push_back(-1);
        }
    }

    //cout << "Rank " << rank << " localConflicts: ";
    //for (int conflict : localConflicts) {
    //    cout << conflict << " ";
    //}
    //cout << endl;
    MPI_Gather(localConflicts.data(), blockSize, MPI_INT, allConflicts.data(), blockSize, MPI_INT, 0, MPI_COMM_WORLD);
}

void Algorithm2Basic::resolveConflictsSequential(const vector<int>& conflicts, vector<int>& colors, const vector<vector<int>>& graph) {
    for (int u : conflicts) {
        set<int> neighborColors;
        for (int neighbor : graph[u]) {
            neighborColors.insert(colors[neighbor]);
        }

        for (int color = 0; color < colors.size(); ++color) {
            if (neighborColors.find(color) == neighborColors.end()) {
                colors[u] = color;
                break;
            }
        }
    }
}

void Algorithm2Basic::algorithm2Basic(vector<vector<int>>& graph) {
    MPI_Barrier(MPI_COMM_WORLD);
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    double start_time, end_time;
    if (rank == 0) {
        start_time = MPI_Wtime();
    }
    int n = graph.size();
    int remainder = n % size;
    int additionalNodes = (remainder == 0) ? 0 : size - remainder;

    for (int i = 0; i < additionalNodes; ++i) {
        graph.push_back({});
    }

    n = n + additionalNodes;

    vector<int> colors(n, -1);
    vector<int> allConflicts(n, -1);
    parallelGreedyColoring(graph, rank, size, colors);
    int colNum = countUniqueColors(colors);
    recolorWithReverseOrdering(graph, rank, size, colors, colNum);
    detectConflicts(graph, rank, size, colors, allConflicts);
    if (rank == 0) {
        allConflicts.erase(remove(allConflicts.begin(), allConflicts.end(), -1), allConflicts.end());
        resolveConflictsSequential(allConflicts, colors, graph);
        end_time = MPI_Wtime();
        double duration = end_time - start_time;

        int numColors = countUniqueColors(colors);
        std::string filename = "C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Results\\algorithm2basic_" + std::to_string(size) + ".txt";
        std::ofstream outfile(filename, std::ios::app);
        if (outfile.is_open()) {
            outfile << "Graph Size: " << n << " vertices" << endl;
            outfile << "Total Colors Used: " << numColors << endl;
            outfile << "Execution Time: " << fixed << setprecision(5) << duration << " s" << endl;

            bool hasConflict = sequentialDetectConflicts(graph, colors);
            if (hasConflict) {
                outfile << "Conflict detected in the coloring!" << endl;
            }
            else {
                outfile << "No conflicts detected in the coloring." << endl;
            }
            outfile << "--------------------------------------" << endl;
        }
        else {
            cerr << "Error: Unable to open file for writing!" << endl;
        }
        outfile.close();
    }

}

void Algorithm2Basic::runAlgorithm2Basic() {
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (rank == 0) {
        std::string filename = "C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Results\\algorithm2basic_" + std::to_string(size) + ".txt";
        std::ofstream outfile(filename, std::ios::app);
        if (outfile.is_open()) {
            outfile << "Algorithm 2 Basic Started ..." << endl;
        }
        else {
            cerr << "Error: Unable to open file for writing!" << endl;
        }
        outfile.close();
    }
    // https://mat.tepper.cmu.edu/COLOR/instances.html
    // https://networkrepository.com/dimacs.php
    std::vector<std::vector<int>> graph;
    if (rank == 0) {
        graph = readGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\games120.col"); // 120 1276
    }
    broadcastGraph(graph, rank, size);
    algorithm2Basic(graph);
    if (rank == 0) {
        graph = readGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\le450_15d.col"); // 450 16750
    }
    broadcastGraph(graph, rank, size);
    algorithm2Basic(graph);
    if (rank == 0) {
        graph = readGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\latin_square_10.col"); // 900 307350
    }
    broadcastGraph(graph, rank, size);
    algorithm2Basic(graph);
    if (rank == 0) {
        graph = readMtxGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\C2000-5.mtx"); // 2000 999836
    }
    broadcastGraph(graph, rank, size);
    algorithm2Basic(graph);
    if (rank == 0) {
        graph = readMtxGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\C4000-5.mtx"); // 4000 4000268
    }
    broadcastGraph(graph, rank, size);
    algorithm2Basic(graph);
    if (rank == 0) {
        std::string filename = "C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Results\\algorithm2basic_" + std::to_string(size) + ".txt";
        std::ofstream outfile(filename, std::ios::app);
        if (outfile.is_open()) {
            outfile << "Algorithm 2 Basic Finished!" << endl;
            outfile << "======================================" << endl;
        }
        else {
            cerr << "Error: Unable to open file for writing!" << endl;
        }
        outfile.close();
    }
}