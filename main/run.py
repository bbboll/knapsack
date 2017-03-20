#!/usr/bin/python3
import robot
import knapsack
import time
import settings

def main():
	"""
	This is the entry point to the program. Abstractions for the Robot,
	Configuration and Knapsack will be instantiated and the main program
	progresses.
	"""
	config = settings.Settings()
	r = robot.Robot(debug=config.debug())
	ks = knapsack.Knapsack(cap=config.knapsack_cap)
	
	# scann all bricks
	while r.waitForBrick():
		color = r.getBrickColor()
		weight, value = config.itemDataForColor(color)
		ks.addItem(weight, value)
		r.dropBrick()
	
	# solve knapsack problem
	max_val, optimal_subset = ks.solve()

	for block_index in range(ks.getItemCount()):
		if block_index in optimal_subset:
			r.throwBrick(trash=False)
		else:
			r.throwBrick(trash=True)

	#r.say("The optimal subset has total value {}".format(max_val))

if __name__ == "__main__":
	main()
