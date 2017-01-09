#ifndef KNAPSACK_H
#define KNAPSACK_H

#include <vector>

// this data type is used when passing the solution
// of a knapsack problem to python
typedef std::vector<int> ItemList;

// struct to hold item data
struct Item {
	int weight;
	int value;
};

// class to hold knapsack problem data and expose solver
class Knapsack
{
private:
	std::vector<Item> items;
	int capacity;

public:
	void addItem(int weight, int value);
	void setCapacity(int cap);
	ItemList solve();
};

#endif