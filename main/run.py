#!/usr/bin/python3
import robot
import knapsack
import time
import settings

# number of bricks that physically fit for a single phase demonstration
MAGAZINE_BRICK_LIMIT = 8

def process_block(r, ks):
	color = r.getBrickColor()
	weight, value = config.itemDataForColor(color)
	ks.addItem(weight, value)
	r.dprint("adding ({},{})".format(weight, value))
	r.dropBrick()
	r.enclosed_brick_count += 1

def demonstration(r, ks, config):
	"""
	Demonstrate the knapsack problem by loading bricks from the magazine, scanning 
	and dropping them. If the user has loaded less than MAGAZINE_BRICK_LIMIT, the 
	scanning process will finish with all bricks still enclosed in the robot.
	It will proceed solving the knapsack problem encoded in the brick color and
	physically output the optimal solution by throwing the bricks in the metaphorical
	knapsack at the bottom of the robot (or the trash).

	If the user has loaded more than MAGAZINE_BRICK_LIMIT, the robot will detect this
	and automatically switch to 'expert mode'. The demonstration becomes two-phased.
	The first phase is the scanning phase; all loaded bricks will instantly be thrown
	out by the robot as soon as they have been scanned.
	The second phase starts on explicit user command (touch sensor). The robot will now
	solve the current knapsack problem while the user (re-)loads all bricks. Sequence of
	(re-)loading is not relevant. The robot will now successively output the optimal solution.
	"""
	for i in range(MAGAZINE_BRICK_LIMIT):
		r.loadBrick()

		# second try for safety
		if not r.checkBrickLoaded():
			r.loadBrick()

		if r.checkBrickLoaded():
			process_block(r, ks)
		else:
			break

	# check if there are more bricks and we have to switch to expert mode
	r.loadBrick()

	# twice, in case a brick gets stuck
	if not r.checkBrickLoaded():
		r.loadBrick()	

	# simple mode if there are MAGAZINE_BRICK_LIMIT or less blocks
	if not r.checkBrickLoaded(): # simple mode
		max_val, optimal_subset = ks.solve()
		r.dprint(optimal_subset)

		# output solution of knapsack problem
		output = []
		for item in ks.items:
			if optimal_subset.count(item) > output.count(item):
				r.throwBrick(trash=False)
				output.append(item)
			else:
				r.throwBrick(trash=True)
			r.enclosed_brick_count -= 1

	# expert mode
	else:
		r.say("Expert mode. Hold button to stop loading bricks.")

		r.outputBricks(r.enclosed_brick_count)
		while not r.buttonIsPressed():
			r.loadBrick()

			if r.checkBrickLoaded():
				process_block(r, ks)

		r.say("Good. Solving knapsack problem.")

		# make sure no blocks are left
		for i in range(2):
			if r.checkBrickLoaded():
				process_block(r, ks)

		max_val, optimal_subset = ks.solve()
		print(optimal_subset)

		r.say("Load all bricks again.")

		leftBlockCount = len(ks.items)
		output = []

		while leftBlockCount != 0 and not r.buttonIsPressed():

			r.loadBrick()
			if r.checkBrickLoaded():

				color = r.getBrickColor()
				weight, value = config.itemDataForColor(color)
				item = [weight, value]
				r.dropBrick()

				# output solution of knapsack problem
				if optimal_subset.count(item) > output.count(item):
					r.throwBrick(trash=False)
					output.append(item)
				else:
					r.throwBrick(trash=True)
					

				r.enclosed_brick_count -= 1
				leftBlockCount -= 1

		# output possibly enclosed bricks
		r.outputBricks(r.enclosed_brick_count)


if __name__ == "__main__":
	# load config, init robot and knapsack
	config = settings.Settings()
	r = robot.Robot(debug=config.debug())
	ks = knapsack.Knapsack(cap=config.knapsack_cap)
	
	# start demonstration if initialization of objects succeeded
	demonstration(r, ks, config)
