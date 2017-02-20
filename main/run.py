#!/usr/bin/python3
import robot
import time

def main():
	r = robot.Robot(debug=True)

	
	r.dropBrick()
	r.dropBrick()
	r.dropBrick()
	r.dropBrick()
	r.dropBrick()

	r.throwBrick(trash=True)
	time.sleep(1)
	r.throwBrick(trash=False)
	time.sleep(1)
	r.throwBrick(trash=False)
	time.sleep(1)
	r.throwBrick(trash=True)
	time.sleep(1)
	r.throwBrick(trash=True)
	
	

	#r.throwBrick(trash=True)
	#r.testBottomMotor()
	#r.testTopMotor()

	#r.waitForBrick()


if __name__ == "__main__":
	main()
