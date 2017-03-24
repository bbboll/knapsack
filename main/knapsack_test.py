#!/usr/bin/python3
import unittest
import knapsack

KNAPSACK_CAP = 10

class TestKnapsackSolver(unittest.TestCase):
	
	def setUp(self):
		"""
        Initiallize knapsack object for testing
        """
		self.knapsack = knapsack.Knapsack(cap=KNAPSACK_CAP)

	def test_capacity(self):
		"""
        Check capacity of knapsack after init
        """
		self.assertEqual(self.knapsack.getCapacity(), KNAPSACK_CAP)

	def test_add_item(self):
		"""
        Test adding items to knapsack
        """
		self.knapsack.addItem(5, 15)
		self.assertEqual(self.knapsack.getItemCount(), 1)
		self.knapsack.addItem(15, -1)
		self.assertEqual(self.knapsack.getItemCount(), 2)
		self.knapsack.addItem(-1, 15)
		self.assertEqual(self.knapsack.getItemCount(), 3)
		self.knapsack.addItem(0, 15)
		self.assertEqual(self.knapsack.getItemCount(), 4)
		self.knapsack.addItem(0, 0)
		self.assertEqual(self.knapsack.getItemCount(), 5)
		self.knapsack.reset()

	def test_solve_one(self):
		"""
		Test a simple example of the knapsack problem
		"""
		self.knapsack.addItem(3, 7)
		self.knapsack.addItem(4, 5)
		self.knapsack.addItem(7, 9)
		self.knapsack.addItem(2, 1)
		self.knapsack.addItem(1, 4)
		value, itemList = self.knapsack.solve()
		self.assertEqual(value, 17)
		self.assertListEqual([[1,4],[2,1],[4,5],[3,7]], itemList)
		self.knapsack.reset()

	def test_solve_two(self):
		"""
		Test of a sample, where every item is too big
		"""
		self.knapsack.addItem(11, 4)
		self.knapsack.addItem(25, 30)
		self.knapsack.addItem(14, 5)
		value, itemList = self.knapsack.solve()
		self.assertEqual(value, 0)
		self.assertListEqual([], itemList)
		self.knapsack.reset()

	def test_solve_three(self):
		"""
		Test of a sample, with items without weight
		"""
		self.knapsack.addItem(0, 5)
		self.knapsack.addItem(0, 4)
		self.knapsack.addItem(0, 7)
		self.knapsack.addItem(0, 2)
		value, itemList = self.knapsack.solve()
		self.assertEqual(value, 18)
		self.assertListEqual([[0,2],[0,7],[0,4],[0,5]], itemList)
		self.knapsack.reset()

	def test_solve_four(self):
		"""
		Test of a sample, where no item has a value
		"""
		self.knapsack.addItem(4, 0)
		self.knapsack.addItem(3, 0)
		self.knapsack.addItem(5, 0)
		self.knapsack.addItem(3, 0)
		value, itemList = self.knapsack.solve()
		self.assertEqual(value, 0)
		self.assertListEqual([], itemList)
		self.knapsack.reset()