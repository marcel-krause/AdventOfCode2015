#!/usr/bin/env python
#Filename: Day17-02.py

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


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 17 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Read the input
	with open('Day17-01_input.dat', 'r', encoding='utf-8') as content_file:
		containerSizes = [int(currLine.replace('\n', '')) for currLine in content_file.readlines()]
	containerSizes.sort(reverse=True)

	# Target value in liters
	targetValue = 150

	# Find out all possible combinations of containers and sum up their volumes
	requiredChars = len(containerSizes)
	numberOfCombinations = 0
	lowestNumberOfContainers = float('inf')
	for i in range(2**len(containerSizes)):
		currBin = bin(i).replace('0b', '')
		missingChars = requiredChars - len(currBin)
		for _ in range(missingChars):
			currBin = '0' + currBin
		currSum = 0
		numberOfContainers = 0
		for j in range(len(currBin)):
			currSum += int(currBin[j])*containerSizes[j]
			numberOfContainers += int(currBin[j])
			if currSum > targetValue:
				break
		if currSum == targetValue:
			if numberOfContainers < lowestNumberOfContainers:
				lowestNumberOfContainers = numberOfContainers
				numberOfCombinations = 0
			numberOfCombinations += 1

	# Print the result
	print('There are {} different combinations to fill {} liters into the minimal amount of {} containers.'.format(numberOfCombinations, targetValue, lowestNumberOfContainers))

	sys.exit()
