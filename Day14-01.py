#!/usr/bin/env python
#Filename: Day14-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       28.01.2020                                                                                      #
#   Copyright:  Copyright (C) 2019, Marcel Krause                                                               #
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
# import json
# import numpy as np
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
#          Classes           #
#----------------------------#
class Reindeer:
	def __init__(self, speed, timing, rest):
		self.speed = speed
		self.timing = timing
		self.rest = rest

	def calcDistance(self, time):
		remainingTime = time
		fullDistance = 0
		while True:
			if remainingTime <= 0:
				break
			if remainingTime >= self.timing + self.rest:
				fullDistance += self.speed * self.timing
				remainingTime -= self.timing + self.rest
			elif remainingTime >= self.timing:
				fullDistance += self.speed * self.timing
				break
			else:
				fullDistance += self.speed * remainingTime
				break

		return(fullDistance)



#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 14 - Riddle 01         |
|                                    |
+------------------------------------+
	''')

	# Specify the total travel time
	travelTime = 2503

	# Read the input
	with open('Day14-01_input.dat', 'r', encoding='utf-8') as content_file:
		data = (content_file.readlines())
		reindeers = []
		for currLine in data:
			reindeerStats = re.findall(r'\d+', currLine)
			reindeers.append(Reindeer(int(reindeerStats[0]), int(reindeerStats[1]), int(reindeerStats[2])))

	# Calculate the distance traveled
	distancesTraveled = []
	for currReindeer in reindeers:
		distancesTraveled.append(currReindeer.calcDistance(travelTime))
	
	# Print the maximal distance traveled by any reindeer
	print(max(distancesTraveled))

	sys.exit()
