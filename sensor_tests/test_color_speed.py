#!/usr/bin/python

import ev3dev.ev3 as ev3
import time

col = ev3.ColorSensor()
touch = ev3.TouchSensor()

col.mode = 'RGB-RAW'
colors = []

print "GO"
start = time.time()

while not touch.value(0):
    colors.append([col.value(0), col.value(1), col.value(2)])

with open("./col_values", "w") as outfile:
    for color in colors:
        outfile.write("R: {:d} G: {:d} B: {:d}\n".format(color[0], color[1], color[2]))
print len(colors)/(time.time()-start)
