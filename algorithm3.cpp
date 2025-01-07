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
#include "algorithm3.h"    
#include <fstream>

using namespace std;
using namespace chrono;
using namespace Algorithm3;


void Algorithm3::parallelGreedyColoring(vector<vector<int>>& graph, int rank, int size, vector<int>& colors) {
    int n = graph.size();
    int blockSize = n / size;

    int start = rank * blockSize;
    int end = (rank == size - 1) ? n : (rank + 1) * blockSize;

    vector<int> localColors(n, -1);
    vector<bool> available(n, true);

    for (int u = start; u < end; ++u) {
        fill(available.begin(), available.end(), true);

        for (int v : graph[u]) {
            if (colors[v] != -1) {
                available[colors[v]] = false;
            }
        }

        for (int color = 0; color < n; ++color) {
            if (available[color]) {
                colors[u] = color;
                break;
            }
        }
    }

}

void Algorithm3::recolorWithReverseOrdering(vector<vector<int>>& graph, int rank, int size, vector<int>& colors) {
    int n = graph.size();
    int blockSize = n / size;

    int start = rank * blockSize;
    int end = (rank == size - 1) ? n : (rank + 1) * blockSize;

    vector<pair<int, int>> vertexColors;
    for (int i = start; i < end; ++i) {
        vertexColors.push_back({ i, colors[i] });
    }

    sort(vertexColors.begin(), vertexColors.end(), [&colors](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second > b.second;
        });

    for (auto& vc : vertexColors) {
        int vertex = vc.first;
        vector<bool> available(n, true);

        for (int neighbor : graph[vertex]) {
            if (colors[neighbor] != -1) {
                available[colors[neighbor]] = false;
            }
        }

        for (int color = 0; color < n; ++color) {
            if (available[color]) {
                colors[vertex] = color;
                break;
            }
        }
    }

}

bool Algorithm3::detectConflicts(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts, bool resolveSmall) {
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

void Algorithm3::resolveConflictsParallel(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts) {
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

void Algorithm3::algorithm3(vector<vector<int>>& graph) {
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
    recolorWithReverseOrdering(graph, rank, size, colors);
    bool hasConflicts = true;
    bool resolveSmall = true;
    int counter = 0;
    while (hasConflicts) {
        int newRank = (rank + counter) % size;
        MPI_Request* sendRequests = new MPI_Request[size];
        MPI_Request* recvRequests = new MPI_Request[size];
        std::fill(sendRequests, sendRequests + size, MPI_REQUEST_NULL);
        std::fill(recvRequests, recvRequests + size, MPI_REQUEST_NULL);
        for (int i = 0; i < size; ++i) {
            if (i != rank) {
                MPI_Isend(colors.data() + newRank * blockSize, blockSize, MPI_INT, i, 0, MPI_COMM_WORLD, &sendRequests[i]);
                MPI_Irecv(colors.data() + i * blockSize, blockSize, MPI_INT, i, 0, MPI_COMM_WORLD, &recvRequests[i]);
            }
        }
        MPI_Waitall(size, sendRequests, MPI_STATUSES_IGNORE);
        MPI_Waitall(size, recvRequests, MPI_STATUSES_IGNORE);
        conflicts.clear();
        bool localHasConflicts = detectConflicts(graph, newRank, size, colors, conflicts, resolveSmall);
        MPI_Request reduceRequest;
        MPI_Iallreduce(&localHasConflicts, &hasConflicts, 1, MPI_C_BOOL, MPI_LOR, MPI_COMM_WORLD, &reduceRequest);
        resolveConflictsParallel(graph, newRank, size, colors, conflicts);
        resolveSmall = !resolveSmall;
        MPI_Wait(&reduceRequest, MPI_STATUS_IGNORE);
        delete[] sendRequests;
        delete[] recvRequests;
        counter += 1;
    }

    MPI_Barrier(MPI_COMM_WORLD);
    if (rank == 0) {
        auto end = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(end - start);
        int numColors = countUniqueColors(colors);
        std::string filename = "C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Results\\algorithm3_" + std::to_string(size) + ".txt";
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


void Algorithm3::runAlgorithm3() {
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (rank == 0) {
        std::string filename = "C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Results\\algorithm3_" + std::to_string(size) + ".txt";
        std::ofstream outfile(filename, std::ios::app);
        if (outfile.is_open()) {
            outfile << "Algorithm 3 Started ..." << endl;
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
    algorithm3(graph);
    if (rank == 0) {
        graph = readGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\le450_15d.col"); // 450 16750
    }
    broadcastGraph(graph, rank, size);
    algorithm3(graph);
    if (rank == 0) {
        graph = readGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\latin_square_10.col"); // 900 307350
    }
    broadcastGraph(graph, rank, size);
    algorithm3(graph);
    if (rank == 0) {
        graph = readMtxGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\C2000-5.mtx"); // 2000 999836
    }
    broadcastGraph(graph, rank, size);
    algorithm3(graph);
    if (rank == 0) {
        graph = readMtxGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\C4000-5.mtx"); // 4000 4000268
    }
    broadcastGraph(graph, rank, size);
    algorithm3(graph);
    if (rank == 0) {
        std::string filename = "C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Results\\algorithm3_" + std::to_string(size) + ".txt";
        std::ofstream outfile(filename, std::ios::app);
        if (outfile.is_open()) {
            outfile << "Algorithm 3 Finished!" << endl;
            outfile << "======================================" << endl;
        }
        else {
            cerr << "Error: Unable to open file for writing!" << endl;
        }
        outfile.close();
    }
}