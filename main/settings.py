#!/usr/bin/python3

class Settings:
	"""
    Settings objects are used to abstract reading and interpreting robot
    settings from `config.json` files.
    """
	knapsack_cap = 10	

	def debug(self):
		"""
    	Return debugging setting provided by user.
    	"""
		return True

	def itemDataForColor(self, color):
		"""
	    Return weight and value specified for the given color (integer code).
	    0: none
        1: black
        2: blue
        3: green
        4: yellow
        5: red
        6: white
        7: brown
	    """
		return 5, 5
