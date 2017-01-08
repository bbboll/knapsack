import knapsack

def main():

	# setup libknapsack object
    capacity = 5
    ks = knapsack.Knapsack(capacity)

    # add items to knapsack
    ks.addItem(0,3,10)
    ks.addItem(1,1,2)
    ks.addItem(2,2,2)
    ks.addItem(3,1,3)

    # print solution
    for item in ks.solve():
        print(item)

if __name__ == "__main__":
    main()