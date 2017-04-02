#!/usr/bin/python

import ev3dev.ev3 as ev3
import time

touch = ev3.TouchSensor()

while not touch.value(0):
    print "hit"
    time.sleep(1)

