#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <set> 
#include <mpi.h>

using namespace std;

std::vector<std::vector<int>> readGraph(const string& filename) {
    ifstream infile(filename);
    if (!infile) {
        cerr << "Can't open the file: " << filename << endl;
        exit(1);
    }

    string line;
    int numVertices = 0, numEdges = 0;
    vector<vector<int>> graph;

    while (getline(infile, line)) {
        if (line.empty() || line[0] == 'c') {
            continue; 
        }
        else if (line[0] == 'p') {
            stringstream ss(line);
            string temp;
            ss >> temp >> temp >> numVertices >> numEdges;
            graph.resize(numVertices);
        }
        else if (line[0] == 'e') {
            stringstream ss(line);
            char temp;
            int u, v;
            ss >> temp >> u >> v;
            // I take the graphs as symmetrical
            // if there is a connection from one vertex to another in coloring problems, they cannot be the same color.
            // Therefore, it does not cause a wrong result
            // It causes extra work for small graphs that I used
            // Because they have two way connections in the file
            // I noticed this too late and since it was only for small graphs I didn't try the results again to fix it.
            // I should used set etc.
            graph[u - 1].push_back(v - 1);
            graph[v - 1].push_back(u - 1);
        }
    }

    infile.close();
    return graph;
}

void printGraph(const std::vector<std::vector<int>>& graph) {
    for (int i = 0; i < graph.size(); ++i) {
        std::cout << i << ": {";
        for (size_t j = 0; j < graph[i].size(); ++j) {
            std::cout << graph[i][j];
            if (j != graph[i].size() - 1) {
                std::cout << ", ";
            }
        }
        std::cout << "}" << std::endl;
    }
}

bool sequentialDetectConflicts(const vector<vector<int>>& graph, const vector<int>& colors) {
    for (int u = 0; u < graph.size(); ++u) {
        for (int v : graph[u]) {
            if (colors[u] == colors[v]) {
                cout << "Conflict detected between Vertex " << u << " and Vertex " << v << endl;
                return true;
            }
        }
    }
    return false;
}

int countUniqueColors(const vector<int>& colors) {
    set<int> uniqueColors(colors.begin(), colors.end());
    return uniqueColors.size();
}

std::vector<std::vector<int>> readMtxGraph(const string& filename) {
    ifstream infile(filename);
    if (!infile) {
        cerr << "Can't open the file: " << filename << endl;
        exit(1);
    }

    string line;
    int numVertices = 0, numEdges = 0;
    vector<vector<int>> graph;

    while (getline(infile, line)) {
        if (line.empty() || line[0] == '%') {
            continue;
        }

        stringstream ss(line);
        ss >> numVertices >> numVertices >> numEdges;

        graph.resize(numVertices); 

        while (getline(infile, line)) {
            stringstream ss(line);
            int u, v;
            ss >> u >> v;
            // I take the graphs as symmetrical
            // if there is a connection from one vertex to another in coloring problems, they cannot be the same color.
            // Therefore, it does not cause a wrong result
            // It causes extra work for small graphs that I used
            // Because they have two way connections in the file
            // I noticed this too late and since it was only for small graphs I didn't try the results again to fix it.
            // I should used set etc.
            graph[u - 1].push_back(v - 1);
            graph[v - 1].push_back(u - 1);
        }
    }

    infile.close();
    return graph;
}

void broadcastGraph(std::vector<std::vector<int>>& graph, int rank, int size) {
    int numNodes = 0;

    if (rank == 0) {
        numNodes = graph.size();
    }

    MPI_Bcast(&numNodes, 1, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank != 0) {
        graph.resize(numNodes);
    }

    for (int i = 0; i < numNodes; ++i) {
        int numEdges = 0;

        if (rank == 0) {
            numEdges = graph[i].size();
        }

        MPI_Bcast(&numEdges, 1, MPI_INT, 0, MPI_COMM_WORLD);

        if (rank != 0) {
            graph[i].resize(numEdges);
        }

        MPI_Bcast(graph[i].data(), numEdges, MPI_INT, 0, MPI_COMM_WORLD);
    }
}