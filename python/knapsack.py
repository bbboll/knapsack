"""
Knapsack objects provide an intuitive means of binding
the problem data 
This example code was taken from http://codereview.stackexchange.com/questions/20569/dynamic-programming-solution-to-knapsack-problem
but is does not seem to work 100%
"""
class Knapsack:
    """
    Initialize new knapsack object
    with capacity and empty items list
    """
    def __init__(self, cap):
        self.capacity = cap
        self.items = []

    """
    add an item to this knapsack list of items
    """
    def addItem(self, weight, value):
        self.items.append([weight, value])

    # Return the value of the most valuable subsequence of the first i
    # elements in items whose weights sum to no more than j.
    def bestvalue(self, i, j):
        if i == 0: return 0
        weight, value = self.items[i - 1]
        if weight > j:
            return self.bestvalue(i - 1, j)
        else:
            return max(self.bestvalue(i - 1, j),
                       self.bestvalue(i - 1, j - weight) + value)

    """
    Solve the knapsack problem by finding the item subset with
    maximum cummulative value whose combined weigth is less than
    the knapsack capacity.
    """
    def solve(self):
        j = self.capacity
        result = []
        for i in xrange(len(self.items), 0, -1):
            if self.bestvalue(i, j) != self.bestvalue(i - 1, j):
                result.append(self.items[i - 1])
                j -= self.items[i - 1][1]
        # result.reverse()
        return self.bestvalue(len(self.items), self.capacity), result