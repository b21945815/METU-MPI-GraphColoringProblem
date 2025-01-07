#ifndef SEQUENTIAL_ALGORITHM_H
#define SEQUENTIAL_ALGORITHM_H

#include <vector>

using namespace std;

void runSequentialAlgorithm();
void iteratedGreedyColoring(vector<vector<int>>& graph);
int greedyColoring(vector<vector<int>>& graph, vector<int>& colors);
void reverseColorClassOrdering(vector<vector<int>>& graph, vector<int>& colors);
bool sequentialDetectConflicts(const vector<vector<int>>& graph, const vector<int>& colors);

#endif