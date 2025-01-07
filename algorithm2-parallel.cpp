#include <mpi.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <set> 
#include <numeric>
#include <chrono>
#include <iomanip>
#include "graph.h"         
#include "algorithm2-parallel.h"    
#include <fstream>

using namespace std;
using namespace chrono;
using namespace Algorithm2Parallel;

void Algorithm2Parallel::parallelGreedyColoring(vector<vector<int>>& graph, int rank, int size, vector<int>& colors) {
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
                break;
            }
        }
    }

    MPI_Gather(localColors.data() + start, blockSize, MPI_INT, colors.data(), blockSize, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Bcast(colors.data(), n, MPI_INT, 0, MPI_COMM_WORLD);

}

void Algorithm2Parallel::recolorWithReverseOrdering(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, int colNum) {
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
                    break;
                }
            }
        }

        MPI_Gather(localColors.data() + rank * blockSize, blockSize, MPI_INT,
            colors.data(), blockSize, MPI_INT, 0, MPI_COMM_WORLD);

        MPI_Bcast(colors.data(), n, MPI_INT, 0, MPI_COMM_WORLD);

    }

}

bool Algorithm2Parallel::detectConflicts(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts, bool resolveSmall) {
    int n = graph.size();
    int blockSize = n / size;

    int start = rank * blockSize;
    int end = (rank == size - 1) ? n : (rank + 1) * blockSize;

    bool hasConflicts = false;
    for (int u = start; u < end; ++u) {
        for (int v : graph[u]) {
            if (colors[u] == colors[v] &&
                ((u < v && resolveSmall) || (u > v && !resolveSmall))) {
                conflicts.push_back(u);
                hasConflicts = true;
                break;
            }
        }
    }
    return hasConflicts;
}

void Algorithm2Parallel::resolveConflictsParallel(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts) {
    int n = graph.size();
    for (int u : conflicts) {
        if (u == -1) continue;

        set<int> neighborColors;
        for (int neighbor : graph[u]) {
            neighborColors.insert(colors[neighbor]);
        }

        for (int color = 0; color < n; ++color) {
            if (neighborColors.find(color) == neighborColors.end()) {
                colors[u] = color;
                break;
            }
        }
    }
}

void Algorithm2Parallel::algorithm2Parallel(vector<vector<int>>& graph) {
    MPI_Barrier(MPI_COMM_WORLD);
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    high_resolution_clock::time_point start;
    if (rank == 0) {
        start = high_resolution_clock::now();
    }
    int n = graph.size();
    int remainder = n % size;
    int additionalNodes = (remainder == 0) ? 0 : size - remainder;

    for (int i = 0; i < additionalNodes; ++i) {
        graph.push_back({});
    }

    n = n + additionalNodes;

    vector<int> colors(n, -1);
    int blockSize = n / size;
    vector<int> conflicts;
    parallelGreedyColoring(graph, rank, size, colors);
    int colNum = countUniqueColors(colors);
    recolorWithReverseOrdering(graph, rank, size, colors, colNum);
    bool hasConflicts = true;
    bool resolveSmall = true;
    while (hasConflicts) {

        MPI_Allgather(MPI_IN_PLACE, blockSize, MPI_INT, colors.data(), blockSize, MPI_INT, MPI_COMM_WORLD);

        conflicts.clear();
        bool localHasConflicts = detectConflicts(graph, rank, size, colors, conflicts, resolveSmall);
        MPI_Allreduce(&localHasConflicts, &hasConflicts, 1, MPI_C_BOOL, MPI_LOR, MPI_COMM_WORLD);
        resolveConflictsParallel(graph, rank, size, colors, conflicts);
        resolveSmall = !resolveSmall;
    }

    MPI_Barrier(MPI_COMM_WORLD);
    if (rank == 0) {
        auto end = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(end - start);
        int numColors = countUniqueColors(colors);
        std::string filename = "C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Results\\algorithm2parallel_" + std::to_string(size) + ".txt";
        std::ofstream outfile(filename, std::ios::app);
        if (outfile.is_open()) {
            outfile << "Graph Size: " << n << " vertices" << endl;
            outfile << "Total Colors Used: " << numColors << endl;
            outfile << "Execution Time: " << fixed << setprecision(3) << duration.count() / 1000.0 << " ms" << endl;

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


void Algorithm2Parallel::runAlgorithm2Parallel() {
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (rank == 0) {
        std::string filename = "C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Results\\algorithm2parallel_" + std::to_string(size) + ".txt";
        std::ofstream outfile(filename, std::ios::app);
        if (outfile.is_open()) {
            outfile << "Algorithm 2 Parallel Started ..." << endl;
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
    algorithm2Parallel(graph);
    if (rank == 0) {
        graph = readGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\le450_15d.col"); // 450 16750
    }
    broadcastGraph(graph, rank, size);
    algorithm2Parallel(graph);
    if (rank == 0) {
        graph = readGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\latin_square_10.col"); // 900 307350
    }
    broadcastGraph(graph, rank, size);
    algorithm2Parallel(graph);
    if (rank == 0) {
        graph = readMtxGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\C2000-5.mtx"); // 2000 999836
    }
    broadcastGraph(graph, rank, size);
    algorithm2Parallel(graph);
    if (rank == 0) {
        graph = readMtxGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\C4000-5.mtx"); // 4000 4000268
    }
    broadcastGraph(graph, rank, size);
    algorithm2Parallel(graph);
    if (rank == 0) {
        std::string filename = "C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Results\\algorithm2parallel_" + std::to_string(size) + ".txt";
        std::ofstream outfile(filename, std::ios::app);
        if (outfile.is_open()) {
            outfile << "Algorithm 2 Parallel Finished!" << endl;
            outfile << "======================================" << endl;
        }
        else {
            cerr << "Error: Unable to open file for writing!" << endl;
        }
        outfile.close();
    }
}