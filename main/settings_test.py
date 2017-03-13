#!/usr/bin/python3
import unittest
import settings

DEFAULT_KS_CAPACITY = 10

class TestSettings(unittest.TestCase):
	
	def setUp(self):
		"""
        Initiallize settings object for testing
        """
		self.settings = settings.Settings()

	def test_debug_setting(self):
		self.assertEqual(self.settings.debug(), True)

	def test_capacity(self):
		"""
        Check capacity of knapsack has loaded from config file
        """
		self.assertEqual(self.settings.knapsack_cap, DEFAULT_KS_CAPACITY)

	def test_color_code(self):
		weight, value = self.settings.itemDataForColor(2)
		self.assertEqual(weight, 4)
		self.assertEqual(value, 15)
		weight, value = self.settings.itemDataForColor(3)
		self.assertEqual(weight, 4)
		self.assertEqual(value, 25)
		weight, value = self.settings.itemDataForColor(4)
		self.assertEqual(weight, 6)
		self.assertEqual(value, 35)
		weight, value = self.settings.itemDataForColor(5)
		self.assertEqual(weight, 2)
		self.assertEqual(value, 15)
		weight, value = self.settings.itemDataForColor(6)
		self.assertEqual(weight, 6)
		self.assertEqual(value, 15)
		weight, value = self.settings.itemDataForColor(7)
		self.assertEqual(weight, 12)
		self.assertEqual(value, 55)