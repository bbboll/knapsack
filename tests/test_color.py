#!/usr/bin/python3

import ev3dev.ev3 as ev3


m = ev3.LargeMotor('outA')
col = ev3.ColorSensor()
touch = ev3.TouchSensor()

m.run_timed(time_sp=2500, speed_sp=150)

print col.modes
col.mode = 'RGB-RAW'

colors = []

while not touch.value(0):
        colors.append([col.value(0), col.value(1), col.value(2)]

