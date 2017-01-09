#include "knapsack.hpp"
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	// init knapsack object
	Knapsack ks;
	ks.setCapacity(5);

	// add items to knapsack problem
	ks.addItem(3,10);
    ks.addItem(1,2);
    ks.addItem(2,2);
    ks.addItem(1,3);

    // solve knapsack
   	ItemList result = ks.solve();
    for (int i = 0; i < result.size(); ++i)
    {
		cout << result.at(i) << endl;    	
    }

	return 0;
}