#!/usr/bin/env python
#Filename: Day06-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       30.12.2018                                                                                      #
#   Copyright:  Copyright (C) 2018, Marcel Krause                                                               #
#   License:    GNU General Public License (GNU GPL-3.0-or-later)                                               #
#                                                                                                               #
#               This program is released under GNU General Public License (GNU GPL-3.0-or-later).               #
#               This program is free software: you can redistribute it and/or modify it under the terms of the  #
#               GNU General Public License as published by the Free Software Foundation, either version 3 of    #
#               the License, or any later version.                                                              #
#                                                                                                               #
#               This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;       #
#               without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.       #
#               See the GNU General Public License for more details.                                            #
#                                                                                                               #
#               You have received a copy LICENSE.md of the GNU General Public License along with this program.  #
#                                                                                                               #
 ###############################################################################################################

#------------------------------#
#         Import Modules       #
#------------------------------#
import sys
import re
# import os
# from shutil import copyfile, rmtree
# from math import pi, sqrt
# import random
# import subprocess

#------------------------------#
#           Settings           #
#------------------------------#


#------------------------------#
#          Functions           #
#------------------------------#


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 06 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Initiate the matrix representing the light field with quadratic size gridSize
	lightsOn = 0
	gridSize = 1000
	lightField = [0] * gridSize
	for x in range(gridSize):
		lightField[x] = [0] * gridSize

	# Read the input file
	with open('Day06-01_input.dat', 'r') as content_file:
		allLines = [line.rstrip('\n') for line in content_file]
		for currLine in allLines:
			regSearch = re.findall(r'(turn off|toggle|turn on) (\d+,\d+) through (\d+,\d+)', currLine)
			if regSearch:
				xStart = int(regSearch[0][1].split(",")[0])
				yStart = int(regSearch[0][1].split(",")[1])
				xEnd = int(regSearch[0][2].split(",")[0])
				yEnd = int(regSearch[0][2].split(",")[1])

				for x in range(xStart, xEnd+1):
					for y in range(yStart, yEnd+1):
						if regSearch[0][0] == "turn off" and lightField[x][y] > 0:
							lightField[x][y] -= 1
						elif regSearch[0][0] == "turn on":
							lightField[x][y] += 1
						elif regSearch[0][0] == "toggle":
							lightField[x][y] += 2

	for x in range(gridSize):
		for y in range(gridSize):
			lightsOn += lightField[x][y]
	
	print(lightsOn)

	sys.exit()
