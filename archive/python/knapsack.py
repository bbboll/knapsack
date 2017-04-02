class Knapsack:
    """
    Knapsack objects provide an intuitive means of binding
    the problem data 
    """
    
    def __init__(self, cap):
        """
        Initialize new knapsack object
        with capacity and empty items list
        """
        self.capacity = cap
        self.items = []

    def setCapacity(self, cap):
        self.capacity = cap
    
    def addItem(self, weight, value):
        """
        add an item to this knapsack list of items
        """
        self.items.append([weight, value])

    
    def findBest(self, i, j):
        """
        Solve the subproblem of finding i items out of the first j items in the pool
        return the optimal (combined) value
        """

        # check for first cache row
        if i == 0: return 0

        # check for cached result
        if self.cache[i][j] >= 0: return self.cache[i][j]

        # grab item for current row
        weight, val = self.items[i-1]

        # check if the current item exceeds weight limit
        # and adjust cache accordingly
        if weight > j:
            # pass down this call
            new = self.findBest(i-1, j)

            # add result to cache
            self.cache[i][j] = new
            return new
        else:
            # candidates for best value
            bestOld = self.findBest(i-1, j)
            bestNew = self.findBest(i-1, j-weight) + val
            new = max(bestOld, bestNew)

            # add result to cache
            self.cache[i][j] = new
            return new

    
    def solve(self):
        """
        Solve the knapsack problem by finding the item subset with
        maximum cummulative value whose combined weigth is less than
        the knapsack capacity.
        """

        # setup cache
        self.cache = [[-1]*(self.capacity+1) for _ in xrange(len(self.items)+1)]
        self.cache[0] = [0 for _ in xrange(self.capacity+1)]

        # fill cache in a non-recursive way
        for i in xrange(len(self.items)+1):
            self.findBest(i, self.capacity)

        # find optimal subset from cached subproblem solutions
        optimalSubset = []
        col = self.capacity
        for i in xrange(len(self.items), 0, -1):
            if self.cache[i][col] != self.cache[i-1][col]:
                col -= self.items[i-1][0]
                optimalSubset.append(self.items[i-1])

        return self.findBest(len(self.items), self.capacity), optimalSubset

