#!/usr/bin/env python
#Filename: Day09-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       11.01.2019                                                                                      #
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
from itertools import permutations
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
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 09 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Read the input file 
	with open('Day09-01_input.dat', 'r', encoding='utf-8') as content_file:
		allLines = [line.rstrip('\n') for line in content_file]

	# Get all distinct cities and their distances from the input file
	allCities = []
	cityMapping = {}
	distanceInput = []
	for currLine in allLines:
		regSearch = re.findall(r'^(\w+)\sto\s(\w+)\s=\s(\d+)$', currLine)
		if regSearch:
			if regSearch[0][0] not in allCities:
				allCities.append(regSearch[0][0])
			if regSearch[0][1] not in allCities:
				allCities.append(regSearch[0][1])
			distanceInput.append([regSearch[0][0], regSearch[0][1], regSearch[0][2]])
	i = 0
	for currCity in allCities:
		cityMapping[currCity] = i
		i += 1

	# Save all distances in a matrix
	numberCities = len(allCities)
	distanceCities = [[0] * numberCities for i in range(numberCities)]
	for currDistance in distanceInput:
		distanceCities[cityMapping[currDistance[0]]][cityMapping[currDistance[1]]] = int(currDistance[2])
		distanceCities[cityMapping[currDistance[1]]][cityMapping[currDistance[0]]] = int(currDistance[2])

	# Calculate the distances of all possible routes
	longestRoute = 0
	allCityList = list(range(0, numberCities))
	for i in range(0, numberCities):
		for j in range(0, numberCities):
			if i != j:
				remainingCities = allCityList[:]
				remainingCities.remove(i)
				remainingCities.remove(j)
				allPermutations = list(permutations(remainingCities))
				for currPermutation in allPermutations:
					currPermutation = list(currPermutation)
					currPermutation.insert(0, i)
					currPermutation.append(j)
					currLength = 0
					for x in range(0, len(currPermutation)-1):
						currLength += distanceCities[currPermutation[x]][currPermutation[x+1]]
					if currLength > longestRoute:
						longestRoute = currLength
	
	print(longestRoute)
	sys.exit()
