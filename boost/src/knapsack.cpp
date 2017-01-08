#include "knapsack.hpp"

// add an item to the pool of items to be considerated for knapsack problem
void Knapsack::addItem(int id, int weight, int value) 
{
	Item nItem;
	nItem.id = id;
	nItem.weight = weight;
	nItem.value = value;
	items.push_back(nItem);
}

// set capacity of knapsack
void Knapsack::setCapacity(int cap)
{
	capacity = cap;
}

// solves the current knapsack problem
ItemList Knapsack::solve() 
{
	// dummy function for testing:
	ItemList mList;
	for (int i = 0; i < items.size(); ++i)
	{
		mList.push_back(items.at(i).id);
	}
	return mList;
}