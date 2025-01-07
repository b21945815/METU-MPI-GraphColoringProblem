#ifndef GRAPH_H
#define GRAPH_H

#include <vector>
#include <string>
#include <set>
#include <iostream>

using namespace std;

std::vector<std::vector<int>> readGraph(const std::string& filename);
std::vector<std::vector<int>> readMtxGraph(const std::string& filename);
void printGraph(const std::vector<std::vector<int>>& graph);
bool sequentialDetectConflicts(const vector<vector<int>>& graph, const vector<int>& colors);
int countUniqueColors(const vector<int>& colors);
void broadcastGraph(std::vector<std::vector<int>>& graph, int rank, int size);

#endif