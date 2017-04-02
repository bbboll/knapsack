#!/usr/bin/python

import ev3dev.ev3 as ev3

col = ev3.ColorSensor()
touch = ev3.TouchSensor()

col.mode = 'RGB-RAW'

while 1:
    red = col.value(0)
    green = col.value(1)
    blue = col.value(2)

    if touch.value(0):
        print "R: ", red, "G: ", green, "B: ", blue

