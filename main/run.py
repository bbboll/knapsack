#!/usr/bin/python3
import robot
import knapsack
import time
import settings

MAGAZINE_BRICK_LIMIT = 5

def singlePhaseDemonstration(r, ks, config):
	"""
	Single phase demonstrations perform scanning of bricks, solving the knapsack problem
	and returning the optimal subset without user intervention. The magazine is expected
	to be loaded.
	"""

	# scan up to MAGAZINE_BRICK_LIMIT bricks
	for _ in range(MAGAZINE_BRICK_LIMIT):
		r.loadBrick()
		if r.checkBrickLoaded():
			color = r.getBrickColor()
			weight, value = config.itemDataForColor(color)
			ks.addItem(weight, value)
			print("adding ({},{})".format(weight, value))
			r.dropBrick()
		else:
			# in case a brick was loaded that could not be detected, drop it 
			# to prevent it from getting stuck in the robot
			ks.addItem(0, 0)
			r.dropBrick()
			break
	
	# solve knapsack problem
	max_val, optimal_subset = ks.solve()
	print(optimal_subset)

	# output solution of knapsack problem
	output = []
	for item in ks.items:
		if optimal_subset.count(item) > output.count(item):
			r.throwBrick(trash=False)
			output.append(item)
		else:
			r.throwBrick(trash=True)
	
def twoPhaseDemonstration(r, ks, config):
	"""
	Two phase demonstrations perform scanning of bricks in the first phase, instantly returing
	each brick to the user. On user command, phase starts. Now, the robot waits for each brick
	to be loaded to the magazine again. It will in turn re-scan each brick and return the optimal
	subset successively.
	"""

def demonstration(r, ks, config):
	"""
	"""
	for i in range(0, MAGAZINE_BRICK_LIMIT):
		r.loadBrick()

		if r.checkBrickLoaded() == True:
			color = r.getBrickColor()
			weight, value = config.itemDataForColor(color)
			ks.addItem(weight, value)
			print("adding ({},{})".format(weight, value))
			r.dropBrick()
		else:
			r.loadBrick() # make sure...
			i -= 1

	# check if there are more bricks and we have to switch to expert mode
	r.loadBrick()
	r.loadBrick() # twice, cause sometings the bricks get stuck

	# beginner mode
	if r.checkBrickLoaded() == False: # beginner mode
		max_val, optimal_subset = ks.solve()
		print(optimal_subset)

		# output solution of knapsack problem
		output = []
		for item in ks.items:
			if optimal_subset.count(item) > output.count(item):
				r.throwBrick(trash=False)
				output.append(item)
			else:
				r.throwBrick(trash=True)

	# expert mode
	else:
		r.say("expert mode...")


if __name__ == "__main__":
	# load config, init robot and knapsack
	config = settings.Settings()
	r = robot.Robot(debug=config.debug())
	ks = knapsack.Knapsack(cap=config.knapsack_cap)
	
	demonstration(r, ks, config)

	#r.say("The optimal subset has total value {}".format(max_val))
