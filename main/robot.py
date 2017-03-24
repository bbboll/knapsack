#!/usr/bin/python3
import time
import sys
import ev3dev.ev3 as ev3

COLOR_NONE 		= 0
COLOR_BLACK		= 1
COLOR_BLUE 		= 2
COLOR_GREEN		= 3
COLOR_YELLOW		= 4
COLOR_RED 		= 5
COLOR_WHITE		= 6
COLOR_BROWN		= 7

class DeviceNotFoundException(Exception):
	pass

class Robot:
	"""
    This is the unified abstraction for all mechanical components
    of the EV3 robot.
    """

	# printing informations for debugging
	debug = True

	# motors	
	loadMotor		= ev3.LargeMotor("outC")
	topMotor		= ev3.MediumMotor("outA")
	bottomMotor 	= ev3.LargeMotor("outB")

	# input sensors
	colorSensor		= ev3.ColorSensor("in1")
	bottomSensor 	= ev3.ColorSensor("in2")
	touchSensor 	= ev3.TouchSensor("in3")	

	# parameters
	DROP_DELAY 			= 1500
	BRICK_WAIT_LIMIT 	= 3000
	LOAD_DELAY			= 500
	LOAD_MOTOR_TIME 	= 750
	LOAD_MOTOR_POWER 	= 300
	TOP_MOTOR_TIME 		= 1000
	BOT_MOTOR_TIME 		= 400
	BOT_MOTOR_POWER 	= 200
	THROW_DELAY		= 500
	COLOR_SENSOR_HERTZ 	= 20
	COLOR_SENSOR_OVERSHOOT  = 50
	TOUCH_SENSOR_HERTZ 	= 5

	def __init__(self, debug=True):
		"""
		Upon initialization, the robot will check if every necessary mechanical
		device is present, center the bottom slate and optionally set itself in debug mode.
		"""
		self.debug = debug
		
		try:
			self.checkDevice(self.loadMotor, "load motor")
			self.checkDevice(self.topMotor, "top motor")
			self.checkDevice(self.bottomMotor, "bottom motor")
			self.checkDevice(self.colorSensor, "top color sensor")
			self.checkDevice(self.bottomSensor, "bottom color sensor")
			self.checkDevice(self.touchSensor, "touch sensor")
		except DeviceNotFoundException as e:
			print(e)
			sys.exit(0)
		
		self.initBottomMotor()
		self.dprint("Robot ready.")

	def checkDevice(self, device, title):
		"""
		Check if a given device is physically connected to the EV3 and responds in
		the expected way. Throws a `DeviceNotFoundException` if any test fails.
		"""
		try:
			self.dprint("Found device '", title, "': ", device.address)
		except Exception as e:
			raise DeviceNotFoundException("Device '{}' not found., ".format(title))

	def say(self, string):
		"""
		Output the handed string via text-to-speech from the EV3.
		"""
		ev3.Sound.speak(string)

	def initBottomMotor(self):
		"""
		Center the bottom slate of the robot. This is necessary for correct operation and will
		automatically be called upon initialization.
		"""
		i = 0

		while self.bottomSensor.color() != COLOR_RED:
			self.runMotor(self.bottomMotor, 75, inversed=(i < 5), power=self.BOT_MOTOR_POWER)
			i += 1	

		if i != 0: # 
			self.runMotor(self.bottomMotor, 50, inversed=(i < 5), power=self.BOT_MOTOR_POWER)		

	def dprint(self, str, var="", var2="", var3="", var4=""):
		"""
		Prints str on the console if debug mode is enabled
		"""
		if self.debug == True:
			print(str, var, var2, var3, var4)

	# sleep in milliseconds
	def sleep(self, milliseconds):
		time.sleep(milliseconds / 1000)

	def getBrickColor(self):
		"""
		Scan brick at top sensor and return color code (integer).
		0: none
		1: black
		2: blue
		3: green
		4: yellow
		5: red
		6: white
		7: brown
		"""
		color = self.colorSensor.color()
		self.dprint("found color: {}".format(color))
		return color

	def loadBrick(self):
		"""
		Loads one brick from the 'magazine' into the main well.
		"""
		self.dprint("loading brick")
		self.runMotor(self.loadMotor, self.LOAD_MOTOR_TIME, power=self.LOAD_MOTOR_POWER)		
		self.runMotor(self.loadMotor, self.LOAD_MOTOR_TIME, power=self.LOAD_MOTOR_POWER, inversed=True)
		self.sleep(self.LOAD_DELAY)

	def checkBrickLoaded(self):
		"""
		Wait for a loaded brick (up to BRICK_WAIT_LIMIT milliseconds). If none is present or the color cannot be detected,
		raise a `BrickNotDetectedException`
		"""
		self.dprint("checking if brick was loaded")
		elapsed = 0
		while(self.colorSensor.color() == COLOR_NONE or self.colorSensor.color() == COLOR_BLACK):
			interval = 1000 / self.COLOR_SENSOR_HERTZ
			self.sleep(interval)
			elapsed += interval
			if elapsed > self.BRICK_WAIT_LIMIT:
				errstr = "Expected brick from magazine but got color: {}".format("black" if self.colorSensor.color() == COLOR_BLACK else "none")
				self.dprint(errstr)
				return False
		return True	

	def dropBrick(self):
		"""
		Drops one brick into the tower by running the top motor for
		TOP_MOTOR_TIME at speed TOP_MOTOR_SPEED and resetting the motor 
		to its previous position.
		"""
		self.dprint("dropping brick")
		self.runMotor(self.topMotor, self.TOP_MOTOR_TIME)
		self.runMotor(self.topMotor, self.TOP_MOTOR_TIME, True)
		self.sleep(self.DROP_DELAY)

	def throwBrick(self, trash=False):
		"""
		Throws one brick out the bottom of the robot. Bricks may be thrown into the knapsack (`trash=False`)
		or into the trash (`trash=True`)
		"""
		self.dprint("throwing into "+("trash" if trash else "knapsack"))
		self.runMotorTillColor(self.bottomMotor, self.bottomSensor, (COLOR_GREEN if trash else COLOR_YELLOW), not trash, self.BOT_MOTOR_POWER)
		self.runMotorTillColor(self.bottomMotor, self.bottomSensor, COLOR_RED, trash, self.BOT_MOTOR_POWER)
		self.sleep(self.THROW_DELAY)

	def runMotor(self, motor, t, inversed=False, power=200):
		"""
		Run given motor clockwise for given time. The power may be specified but is expected to
		be positive. Pass `inversed=True` to move counter-clockwise.
		"""
		motor.reset()
		motor.run_timed(time_sp=t, speed_sp=power * (-1 if inversed else 1))
		while True:
			self.sleep(500)
			if not 'running' in motor.state:
				return

	def runMotorTillColor(self, motor, sensor, color, inversed=False, power=200):
		"""
		Runs given motor clockwise until given sensor detects specified color or a timeout is triggered. Power may be 
		specified and is expected to be positive. Pass `inversed=True` to move counter-clockwise.
		"""
		motor.reset()
		motor.run_forever(speed_sp=power * (-1 if inversed else 1))
		end = 0
		while sensor.color() != color and end < 20:
			self.sleep(20)
			end = end + 1
		self.sleep(self.COLOR_SENSOR_OVERSHOOT)
		motor.stop()

	def waitForTouch(self):
		"""
		Blocks the current thread until touch sensor is pressed.
		"""
		while(self.touchSensor.value() != 1):
			self.dprint("Waiting for button press... Status: Not Pressed")
			self.sleep(1000 / self.TOUCH_SENSOR_HERTZ) # let the robot relax
		self.dprint("Waiting for button press... Status: Pressed")

	def buttonIsPressed(self):
		return self.touchSensor.value() == 1

