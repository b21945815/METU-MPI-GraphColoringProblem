#ifndef ALGORITHM_2_HALF_ASYNCHRONOUS_H
#define ALGORITHM_2_HALF_ASYNCHRONOUS_H

#include <vector>

using namespace std;
namespace Algorithm2HalfAsynchronous {
	void algorithm2HalfAsynchronous(vector<vector<int>>& graph);
	void runAlgorithm2HalfAsynchronous();
	void parallelGreedyColoring(vector<vector<int>>& graph, int rank, int size, vector<int>& colors);
	void recolorWithReverseOrdering(vector<vector<int>>& graph, int rank, int size, vector<int>& colors);
	bool detectConflicts(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts, bool resolveSmall);
	void resolveConflictsParallel(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts);
}

#endif