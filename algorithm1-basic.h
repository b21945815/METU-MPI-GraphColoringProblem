#ifndef ALGORITHM_1_BASIC_H
#define ALGORITHM_1_BASIC_H

#include <vector>

using namespace std;
namespace Algorithm1Basic{
	void parallelGreedyColoring(vector<vector<int>>& graph, int rank, int size, vector<int>& colors);
	void detectConflicts(vector<vector<int>>& graph, int rank, int size, vector<int>& colors, vector<int>& allConflicts);
	void resolveConflictsSequential(const vector<int>& conflicts, vector<int>& colors, const vector<vector<int>>& graph);
	void algorithm1Basic(vector<vector<int>>& graph);
	void runAlgorithm1Basic();
}

#endif