#ifndef ALGORITHM_2_PARALLEL_H
#define ALGORITHM_2_PARALLEL_H

#include <vector>

using namespace std;
namespace Algorithm2Parallel {
	void algorithm2Parallel(vector<vector<int>>& graph);
	void runAlgorithm2Parallel();
	void parallelGreedyColoring(vector<vector<int>>& graph, int rank, int size, vector<int>& colors);
	void recolorWithReverseOrdering(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, int colNum);
	bool detectConflicts(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts, bool resolveSmall);
	void resolveConflictsParallel(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts);
}

#endif