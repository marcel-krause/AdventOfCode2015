#!/usr/bin/env python
#Filename: Day18-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       21.12.2020                                                                                      #
#   Copyright:  Copyright (C) 2021, Dr. Marcel Krause                                                           #
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


#------------------------------#
#          Functions           #
#------------------------------#
# Displays the current configuration in a (row, col) grid
def displayConfig(lightConfiguration):
	fullDisplay = ''
	for row in lightConfiguration:
		for col in row:
			fullDisplay += '#' if col==1 else '.'
		fullDisplay += '\n'
	print(fullDisplay.strip())

# Gets the values of the neighbooring entries of entry (row, col) of the configuration grid. If (row, col) is at the edge, the non-existent points "beyond" the grid are set to zero. Sums up all values and returns the amount of all neighbooring lights that are 'on'
def countNeighbors(lightConfiguration, row, col):
	neighborVals = []
	for i in range(row-1, row+2):
		for j in range(col-1, col+2):
			if i == row and j == col:
				continue
			if i < 0 or j < 0 or i >= len(lightConfiguration) or j >= len(lightConfiguration[0]):
				neighborVals.append(0)
			else:
				neighborVals.append(lightConfiguration[i][j])
	return sum(neighborVals)

# Updates the grid
def updateConfig(lightConfiguration):
	lightConfigurationNew = []
	for i in range(len(lightConfiguration)):
		tmp = []
		for j in range(len(lightConfiguration[0])):
			# Set corner lights to always on
			# if (i == 0 and j == 0) or (i == 0 and j == len(lightConfiguration[0])-1) or (i == len(lightConfiguration)-1 and j == 0) or (i == len(lightConfiguration)-1 and len(lightConfiguration[0])-1):
			# 	tmp.append(1)
			# 	continue
			numNeighborOn = countNeighbors(lightConfiguration, i, j)
			if lightConfiguration[i][j] == 1:
				if numNeighborOn == 2 or numNeighborOn == 3:
					tmp.append(1)
				else:
					tmp.append(0)
			else:
				if numNeighborOn == 3:
					tmp.append(1)
				else:
					tmp.append(0)
		lightConfigurationNew.append(tmp)
	return lightConfigurationNew

# Count all active lights in the grid
def countLights(lightConfiguration):
	allLights = 0
	for i in range(len(lightConfiguration)):
		for j in range(len(lightConfiguration[0])):
			allLights += lightConfiguration[i][j]
	return allLights

#----------------------------#
#          Classes           #
#----------------------------#


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 18 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Read the input
	with open('Day18-01_input.dat', 'r', encoding='utf-8') as content_file:
		lightConfiguration = []
		for currLine in content_file.readlines():
			currLineStripped = currLine.replace('\n', '')
			lightConfiguration.append([0 if currElem=='.' else 1 for currElem in currLineStripped])
		# Set the corner lights to always on
		lightConfiguration[0][0] = 1
		lightConfiguration[0][len(lightConfiguration[0])-1] = 1
		lightConfiguration[len(lightConfiguration)-1][0] = 1
		lightConfiguration[len(lightConfiguration)-1][len(lightConfiguration[0])-1] = 1

	# Update the configuration
	currLightConfiguration = lightConfiguration
	maxSteps = 100
	for i in range(maxSteps+1):
		if i == 0:
			print('\nInitial state:')
			displayConfig(currLightConfiguration)
			print('Number of active lights: {}'.format(countLights(currLightConfiguration)))
		else:
			currLightConfiguration = updateConfig(currLightConfiguration)
			# Set the corner lights to always on
			currLightConfiguration[0][0] = 1
			currLightConfiguration[0][len(currLightConfiguration[0])-1] = 1
			currLightConfiguration[len(currLightConfiguration)-1][0] = 1
			currLightConfiguration[len(currLightConfiguration)-1][len(currLightConfiguration[0])-1] = 1
			print('\nAfter step {}:'.format(i))
			displayConfig(currLightConfiguration)
			print('Number of active lights: {}'.format(countLights(currLightConfiguration)))

	sys.exit()
