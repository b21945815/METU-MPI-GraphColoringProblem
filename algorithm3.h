#ifndef ALGORITHM_3_H
#define ALGORITHM_3_H

#include <vector>

using namespace std;
namespace Algorithm3 {
	void algorithm3(vector<vector<int>>& graph);
	void runAlgorithm3();
	void parallelGreedyColoring(vector<vector<int>>& graph, int rank, int size, vector<int>& colors);
	void recolorWithReverseOrdering(vector<vector<int>>& graph, int rank, int size, vector<int>& colors);
	bool detectConflicts(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts, bool resolveSmall);
	void resolveConflictsParallel(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& conflicts);
}

#endif