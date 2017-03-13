#!/usr/bin/python3
import unittest
import knapsack

KNAPSACK_CAP = 10

class TestKnapsackSolver(unittest.TestCase):
	
	def setUp(self):
		self.knapsack = knapsack.Knapsack(cap=KNAPSACK_CAP)

	def test_capacity(self):
		self.assertEqual(self.knapsack.getCapacity(), KNAPSACK_CAP)

	def test_add_item(self):
		self.knapsack.addItem(5, 15)
		self.assertEqual(self.knapsack.getItemCount(), 1)