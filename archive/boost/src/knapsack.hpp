#ifndef KNAPSACK_H
#define KNAPSACK_H

#include <vector>

// struct to hold item data
struct Item {
	int weight;
	int value;
};

// this data type is used when passing the solution
// of a knapsack problem to python
typedef std::vector<Item> ItemList;

// class to hold knapsack problem data and expose solver
class Knapsack
{
private:
	std::vector<Item> items;
	int **cache;
	int capacity;
	int findBest(int i, int j);

public:
	void addItem(int weight, int value);
	void setCapacity(int cap);
	ItemList solve();
};

#endif