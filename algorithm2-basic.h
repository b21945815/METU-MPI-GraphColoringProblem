#ifndef ALGORITHM_2_BASIC_H
#define ALGORITHM_2_BASIC_H

#include <vector>

using namespace std;
namespace Algorithm2Basic {
	void parallelGreedyColoring(vector<vector<int>>& graph, int rank, int size, vector<int>& colors);
	void recolorWithReverseOrdering(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, int colNum);
	void detectConflicts(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& allConflicts);
	void resolveConflictsSequential(const vector<int>& conflicts, vector<int>& colors, const vector<vector<int>>& graph);
	void algorithm2Basic(vector<vector<int>>& graph);
	void runAlgorithm2Basic();
}
#endif