import knapsack
import time

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

    # benchmark first small example
    ks.setCapacity(5);
    ks.addItem(3,10);
    ks.addItem(1,2);
    ks.addItem(2,2);
    ks.addItem(1,3);

    start = time.clock()
    result = ks.solve()
    duration_small_one = (time.clock()-start)
    print "cap: 5, items: 4. took: ", duration_small_one, " seconds."
   
   # benchmark second small example
    ks.setCapacity(7);
    ks.addItem(3,10)
    ks.addItem(2,1);

    start = time.clock()
    result = ks.solve()
    duration_small_two = (time.clock()-start)
    print "cap: 7, items: 6. took: ", duration_small_two, " seconds."
    

    # benchmark first medium example
    ks.setCapacity(89);
    ks.addItem(3,14);
    ks.addItem(2,1);
    ks.addItem(3,30);
    ks.addItem(2,14);
    ks.addItem(3,10);
    ks.addItem(5,6);
    ks.addItem(42,10);
    ks.addItem(7,23);
    ks.addItem(9,10);
    ks.addItem(1,3);
    ks.addItem(4,10);
    ks.addItem(32,7);
    ks.addItem(3,10);
    ks.addItem(1,2);
    ks.addItem(6,10);
    ks.addItem(3,54);
    ks.addItem(3,12);
    ks.addItem(5,13);
    ks.addItem(51,11);
    ks.addItem(4,42);
    ks.addItem(9,52);
    ks.addItem(24,2);
    ks.addItem(4,10);
    ks.addItem(63,17);

    start = time.clock()
    result = ks.solve()
    duration_medium_two = (time.clock()-start)
    print "cap: 89, items: 30. took: ", duration_medium_two, " seconds."

    # benchmark second medium example
    ks.setCapacity(102);
    ks.addItem(3,13);
    ks.addItem(53,10);
    ks.addItem(4,42);
    ks.addItem(23,62);
    ks.addItem(1,19);

    start = time.clock()
    result = ks.solve()
    duration_medium_two = (time.clock()-start)
    print "cap: 102, items: 35. took: ", duration_medium_two, " seconds."

    # benchmark first big example
    ks.setCapacity(130);
    ks.addItem(3,14);
    ks.addItem(2,1);
    ks.addItem(3,30);
    ks.addItem(2,12);
    ks.addItem(3,10);
    ks.addItem(5,6);
    ks.addItem(42,10);
    ks.addItem(7,24);
    ks.addItem(9,53);
    ks.addItem(6,65);
    ks.addItem(4,4);
    ks.addItem(32,12);
    ks.addItem(3,53);
    ks.addItem(2,3);
    ks.addItem(6,53);
    ks.addItem(3,2);
    ks.addItem(12,1);
    ks.addItem(5,43);
    ks.addItem(51,11);
    ks.addItem(4,53);
    ks.addItem(23,3);
    ks.addItem(24,6);
    ks.addItem(1,2);
    ks.addItem(6,10);
    ks.addItem(7,5);
    ks.addItem(41,23);
    ks.addItem(4,13);
    ks.addItem(51,11);
    ks.addItem(2,45);
    ks.addItem(9,53);
    ks.addItem(8,1);
    ks.addItem(23,13);
    ks.addItem(42,10);
    ks.addItem(7,24);
    ks.addItem(8,32);
    ks.addItem(3,65);
    ks.addItem(4,4);
    ks.addItem(2,2);
    ks.addItem(41,53);
    ks.addItem(7,33);
    ks.addItem(2,53);

    start = time.clock()
    result = ks.solve()
    duration_big_two = (time.clock()-start)
    print "cap: 130, items: 76. took: ", duration_big_two, " seconds."
    

    # benchmark second big example
    ks.setCapacity(150);
    ks.addItem(2,13);
    ks.addItem(53,154);
    ks.addItem(14,442);
    ks.addItem(23,2);
    ks.addItem(2,42);
    ks.addItem(53,123);
    ks.addItem(2,12);

    start = time.clock()
    result = ks.solve()
    duration_big_two = (time.clock()-start)
    print "cap: 150, items: 83. took: ", duration_big_two, " seconds."

if __name__ == "__main__":
    main()