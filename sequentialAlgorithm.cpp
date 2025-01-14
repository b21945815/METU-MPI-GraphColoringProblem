#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>
#include "graph.h"         
#include "sequentialAlgorithm.h"      
#include <fstream>

using namespace std;
using namespace chrono;


int greedyColoring(vector<vector<int>>& graph, vector<int>& colors) {
    int n = graph.size();
    int maxColor = 0;

    fill(colors.begin(), colors.end(), -1);

    for (int u = 0; u < n; ++u) {
        vector<bool> available(n, true);

        for (int v : graph[u]) {
            if (colors[v] != -1) {
                available[colors[v]] = false;
            }
        }

        int color;
        for (color = 0; color < n; ++color) {
            if (available[color]) {
                break;
            }
        }
        colors[u] = color;
        maxColor = max(maxColor, color);
    }

    return maxColor + 1;
}

void reverseColorClassOrdering(vector<vector<int>>& graph, vector<int>& colors) {
    vector<vector<int>> colorClasses(*max_element(colors.begin(), colors.end()) + 1);
    for (int i = 0; i < graph.size(); ++i) {
        colorClasses[colors[i]].push_back(i);
    }

    vector<int> reverseOrder;
    for (int i = colorClasses.size() - 1; i >= 0; --i) {
        reverseOrder.insert(reverseOrder.end(), colorClasses[i].begin(), colorClasses[i].end());
    }

    vector<int> newColors(graph.size(), -1);
    for (int i = 0; i < reverseOrder.size(); ++i) {
        int u = reverseOrder[i];
        vector<bool> available(graph.size(), true);

        for (int v : graph[u]) {
            if (newColors[v] != -1) {
                available[newColors[v]] = false;
            }
        }

        int color;
        for (color = 0; color < graph.size(); ++color) {
            if (available[color]) {
                break;
            }
        }
        newColors[u] = color;
    }

    colors = newColors;
}

void iteratedGreedyColoring(vector<vector<int>>& graph) {
    auto start = high_resolution_clock::now();
    int n = graph.size();
    vector<int> colors(n);
    int ColNum = greedyColoring(graph, colors);
    // cout << "Phase 1 (Greedy Coloring) - Number of Colors: " << ColNum << endl;
    int maxIterations = 200;
    int noImprovementThreshold = 5;
    int iterationsWithoutImprovement = 0;
    int lastColNum = ColNum;

    for (int iteration = 0; iteration < maxIterations; ++iteration) {
        reverseColorClassOrdering(graph, colors);

        int currentColNum = *max_element(colors.begin(), colors.end()) + 1;

 
        if (currentColNum < lastColNum) {
            lastColNum = currentColNum;
            iterationsWithoutImprovement = 0; 
        }
        else {
            ++iterationsWithoutImprovement; 
        }

        if (iterationsWithoutImprovement >= noImprovementThreshold) {
            cout << "Early stopping triggered after " << iteration + 1 << " iterations." << endl;
            break;
        }
    }

    auto end = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(end - start);

    // Final result
    //cout << "Final Coloring:" << endl;
    //for (int i = 0; i < n; ++i) {
    //    cout << "Vertex " << i << ": Color " << colors[i] << endl;
    //}
    std::ofstream outfile("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Results\\iteratedGreedyColoring.txt", std::ios::app);
    if (outfile.is_open()) {
        outfile << "Graph Size: " << n << " vertices" << endl;
        outfile << "Total Colors Used: " << lastColNum << endl;
        outfile << "Execution Time: " << fixed << setprecision(5) << duration.count() / 1000000.0 << " s" << endl;

        bool hasConflict = sequentialDetectConflicts(graph, colors);
        if (hasConflict) {
            outfile << "Conflict detected in the coloring!" << endl;
        }
        else {
            outfile << "No conflicts detected in the coloring." << endl;
        }
        outfile << "--------------------------------------" << endl;
    } else {
        cerr << "Error: Unable to open file for writing!" << endl;
    }
    outfile.close();

}

void runSequentialAlgorithm() {
    std::ofstream outfile("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Results\\iteratedGreedyColoring.txt", std::ios::app); 
    if (outfile.is_open()) {
        outfile << "Sequential Algorithm Started..." << endl;
    } else {
        cerr << "Error: Unable to open file for writing!" << endl;
    }
    outfile.close();
    // https://mat.tepper.cmu.edu/COLOR/instances.html
    // https://networkrepository.com/dimacs.php
    std::vector<std::vector<int>> graph = readGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\games120.col"); // 120 1276
    iteratedGreedyColoring(graph);
    graph = readGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\le450_15d.col"); // 450 16750
    iteratedGreedyColoring(graph);
    graph = readGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\latin_square_10.col"); // 900 307350
    iteratedGreedyColoring(graph);
    graph = readMtxGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\C2000-5.mtx"); // 2000 999836
    iteratedGreedyColoring(graph);
    graph = readMtxGraph("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Graphs\\C4000-5.mtx"); // 4000 4000268
    iteratedGreedyColoring(graph);
    // printGraph(graph);
    std::ofstream outfile2("C:\\Users\\fatih\\source\\repos\\TRIAL_1\\Results\\iteratedGreedyColoring.txt", std::ios::app);
    if (outfile2.is_open()) {
        outfile2 << "Sequential Algorithm Finished!" << endl;
        outfile2 << "======================================" << endl; 
    } else {
        cerr << "Error: Unable to open file for writing!" << endl;
    }
    outfile2.close();
}