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