#!/usr/bin/python3

import time
import sys
import ev3dev.ev3 as ev3

COLOR_RED = 5

class DeviceNotFoundException(Exception):
	pass
	

class Robot:

	# printing informations for debugging
	debug = True

	# motors	
	topMotor	= ev3.MediumMotor("outA")
	bottomMotor 	= ev3.LargeMotor("outB")

	# input sensors
	colorSensor	= ev3.ColorSensor("in1")
	bottomSensor 	= ev3.ColorSensor("in2")
	touchSensor 	= ev3.TouchSensor("in3")	

	# parameters
	DROP_DELAY = 1500
	TOP_MOTOR_TIME = 750
	BOT_MOTOR_TIME = 400
	BOT_MOTOR_POWER = 200
	COLOR_SENSOR_HERTZ = 20
	TOUCH_SENSOR_HERTZ = 5

	def __init__(self, debug=True):
		self.debug = debug
		
		try:
			self.checkDevice(self.topMotor, "top motor")
			self.checkDevice(self.bottomMotor, "bottom motor")
			self.checkDevice(self.colorSensor, "top color sensor")
			self.checkDevice(self.bottomSensor, "bottom color sensor")
			self.checkDevice(self.touchSensor, "touch sensor")
		except DeviceNotFoundException as e:
			print(e)
			sys.exit(0)
		
		self.initBottomMotor()
		self.dprint("Ready.")
		# ev3.Sound.speak("Trucks are bad, mkay you fucking cunt?")

	def checkDevice(self, device, title):
		try:
			self.dprint("Found device '", title, "': ", device.address)
		except Exception as e:
			raise DeviceNotFoundException("Device '{}' not found., ".format(title))

	def initBottomMotor(self):
		i = 0

		while self.bottomSensor.color() != COLOR_RED:
			self.runMotor(self.bottomMotor, 75, inversed=(i < 5), power=self.BOT_MOTOR_POWER)
			i += 1	

		if i != 0: # 
			self.runMotor(self.bottomMotor, 50, inversed=(i < 5), power=self.BOT_MOTOR_POWER)		

	# prints str on the console if debug mode is enabled
	def dprint(self, str, var="", var2="", var3="", var4=""):
		if self.debug == True:
			print(str, var, var2, var3, var4)

	# sleep in milliseconds
	def sleep(self, milliseconds):
		time.sleep(milliseconds / 1000)
	
	#
	def waitForTouch(self):
		while(self.touchSensor.value() != 1):
			self.dprint("Waiting for button press... Status: Not Pressed")
			self.sleep(1000 / self.TOUCH_SENSOR_HERTZ) # let the robot relax
		self.dprint("Waiting for button press... Status: Pressed")

	# wait for a brick
	def waitForBrick(self):
		self.dprint("Waiting for brick")
		while(True):
			self.sleep(1000 / self.COLOR_SENSOR_HERTZ)
			print(self.colorSensor.color())

	# 750 milliseconds at 200 sp
	def dropBrick(self):
		self.dprint("dropping brick")
		self.runMotor(self.topMotor, self.TOP_MOTOR_TIME)
		self.runMotor(self.topMotor, self.TOP_MOTOR_TIME, True)
		self.sleep(self.DROP_DELAY)

	# 
	def throwBrick(self, trash=False):
		self.runMotor(self.bottomMotor, self.BOT_MOTOR_TIME, inversed=trash, power=self.BOT_MOTOR_POWER)

		# center motor
		while(self.bottomSensor.color() != COLOR_RED):		
			self.runMotorTillRed(self.bottomMotor, self.bottomSensor, inversed=(not trash),power=self.BOT_MOTOR_POWER)
		self.runMotor(self.bottomMotor, 75, inversed=(not trash),power=self.BOT_MOTOR_POWER)


	def runMotor(self, motor, t, inversed=False, power=200):
		motor.reset()
		motor.run_timed(time_sp=t, speed_sp=power * (-1 if inversed else 1))
		while True:
			self.sleep(500)
			if not 'running' in motor.state:
				return

	def runMotorTillRed(self, motor, sensor, inversed=False, power=200):
		motor.reset()
		motor.run_forever(speed_sp=power * (-1 if inversed else 1))

		while sensor.color() != COLOR_RED:
			motor.stop()
			return		


