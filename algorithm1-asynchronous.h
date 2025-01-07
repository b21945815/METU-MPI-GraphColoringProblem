#ifndef ALGORITHM_1_ASYNCHRONOUS_H
#define ALGORITHM_1_ASYNCHRONOUS_H

#include <vector>

using namespace std;
namespace Algorithm1Asynchronous {
	void algorithm1Asynchronous(vector<vector<int>>& graph);
	void runAlgorithm1Asynchronous();
	void parallelGreedyColoring(vector<vector<int>>& graph, int rank, int size, vector<int>& colors);
	bool detectConflicts(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts, bool resolveSmall);
	void resolveConflictsParallel(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts);
}

#endif