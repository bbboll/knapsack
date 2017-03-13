#!/usr/bin/python3
import os.path
import os
import json

CONFIG_FILENAME = "./config.json"
DEFAULT_CONFIG_FILENAME = "./config_default.json"
COLOR_CODES = {0: "none", 1: "black", 2: "blue", 3: "green", 4: "yellow", 5: "red", 6: "white", 7: "brown"}

class ConfigInaccessibleException(Exception):
	pass

class Settings:
	"""
	Settings objects are used to abstract reading and interpreting robot
	settings from `config.json` files.
	"""
	knapsack_cap = 10
	config = {}
	debug_setting = True

	def __init__(self):
		"""
		Upon initialization, a `config.json` file will be loaded. If none is present (and readable), 
		attempt a fallback to `config_default.json`. If no config file could be found and read,
		raise a ConfigInaccessibleException.
		"""

		# try `config.json` and fall back to `config_default.json`
		config_filepath = ""
		if os.path.isfile(CONFIG_FILENAME) and os.access(CONFIG_FILENAME, os.R_OK):
			# load user config file
			config_filepath = CONFIG_FILENAME
		elif os.path.isfile(DEFAULT_CONFIG_FILENAME) and os.access(DEFAULT_CONFIG_FILENAME, os.R_OK):
			print("No readable config file provided, falling back to default config.")
			# load default config file
			config_filepath = DEFAULT_CONFIG_FILENAME

		# make sure a config file was found
		if config_filepath == "":
			raise ConfigInaccessibleException("No readable config.json could be found.")
			return

		# load config from file
		with open(config_filepath) as config_file:
			conf = json.load(config_file)

			if "capacity" not in conf:
				raise ConfigInaccessibleException("Invalid config file. Knapsack capacity needs to be specified.")
				return
			self.knapsack_cap = conf["capacity"]

			if "debug" in conf:
				self.debug_setting = conf["debug"]

			if "bricks" not in conf:
				return
			for item in conf["bricks"]:
				self.config[item["color"]] = {"weight": item["weight"], "value": item["value"]}

	def debug(self):
		"""
		Return debugging setting provided by user. If none was provided, default to `True`.
		"""
		return self.debug_setting

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
		If the desired color is not specified in the user config, returns 0, 0 
		effectively ignoring the color in question.
		"""
		if color in COLOR_CODES:
			col_str = COLOR_CODES[color]
			if col_str in self.config:
				col_conf = self.config[col_str]
				return col_conf["weight"], col_conf["value"]


		return 0, 0
