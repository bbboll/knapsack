#include "knapsack.hpp"

// add an item to the pool of items to be considerated for knapsack problem
void Knapsack::addItem(int weight, int value) 
{
	Item nItem;
	nItem.weight = weight;
	nItem.value = value;
	items.push_back(nItem);
}

// Solve the subproblem of finding i items out of the first j items in the pool
// return the optimal (combined) value
int Knapsack::findBest(int i, int j)
{
	// check for first row
	if (i == 0) {return 0;}

	// check for cached result
	if (cache[i][j] >= 0) {return cache[i][j];}

	// grab item for current row
	int weight = items.at(i-1).weight;
	int val = items.at(i-1).value;

	// check if the current item exceeds weight limit
	// and adjust cache accordingly
	if (weight > j)
	{
		// pass down this call
        int n = findBest(i-1, j);

        // add result to cache
        cache[i][j] = n;
        return n;
	}
	// candidates for best value
    int bestOld = findBest(i-1, j);
    int bestNew = findBest(i-1, j-weight) + val;
    int n = bestNew;
    if (bestOld > bestNew) {n = bestOld;}

    // add result to cache
    cache[i][j] = n;
    return n;
}

void Knapsack::setCapacity(int cap) {capacity = cap;}

ItemList Knapsack::solve() 
{
	// init cache
	cache = new int*[items.size()+1];
	cache[0] = new int[capacity+1];
	for (int j=0; j<capacity+1; ++j) {cache[0][j] = 0;}
	for (int i=1; i<items.size()+1; ++i)
	{
		cache[i] = new int[capacity+1];
		for (int j=0; j<capacity+1; ++j) {cache[i][j] = -1;}
	}

	// fill cache in a non-recursive way
	for (int i=0; i<items.size()+1; ++i) {findBest(i, capacity);}

	// find optimal subset from cached subproblem solutions
    ItemList optimalSubset;
    int col = capacity;
    for (int i=items.size(); i>0; --i)
    {
    	if (cache[i][col] != cache[i-1][col])
    	{
    		col -= items.at(i-1).weight;
            optimalSubset.push_back(items.at(i-1));
    	}
    }

	return optimalSubset;
}