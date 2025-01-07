#ifndef ALGORITHM_1_HALF_ASYNCHRONOUS_H
#define ALGORITHM_1_HALF_ASYNCHRONOUS_H

#include <vector>

using namespace std;
namespace Algorithm1HalfAsynchronous {
	void algorithm1HalfAsynchronous(vector<vector<int>>& graph);
	void runAlgorithm1HalfAsynchronous();
	void parallelGreedyColoring(vector<vector<int>>& graph, int rank, int size, vector<int>& colors);
	bool detectConflicts(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts, bool resolveSmall);
	void resolveConflictsParallel(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts);
}

#endif