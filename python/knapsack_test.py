import knapsack

"""
This script is used to debug the knapsack solver in python/knapsack.py
"""
def main():

	# setup libknapsack object
    capacity = 5
    ks = knapsack.Knapsack(capacity)

    # add items to knapsack
    ks.addItem(3,10)
    ks.addItem(1,2)
    ks.addItem(2,2)
    ks.addItem(1,3)

    # print solution
    for item in ks.solve():
        print(item)

if __name__ == "__main__":
    main()