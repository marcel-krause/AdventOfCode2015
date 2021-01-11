#!/usr/bin/env python
#Filename: Day13-01.py

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
import re
import itertools
from math import sqrt


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 13 - Riddle 01         |
|                                    |
+------------------------------------+
	''')

	# Read the input
	with open('Day13-01_input.dat', 'r', encoding='utf-8') as content_file:
		allLines = content_file.readlines()
		lineCount = len(allLines)
		numberOfGuests = int((1+sqrt(1+4*lineCount))/2)
		currLineCount = 0
		personCount = 0
		personBlockCount = 0
		guestMatrix = []
		for currLine in allLines:
			if currLineCount == 0:
				tmp = []
			if personBlockCount == personCount:
				tmp.append(0)
			currLineCount += 1
			personBlockCount += 1
			reFind = re.search(r'(gain\b|lose)?\s(\d+) happiness', currLine)
			if reFind.group(1) == 'gain':
				tmp.append(int(reFind.group(2)))
			else:
				tmp.append(-1*int(reFind.group(2)))
			if currLineCount == lineCount:
				tmp.append(0)
			if currLineCount%(numberOfGuests-1) == 0:
				guestMatrix.append(tmp)
				tmp = []
				personCount += 1
				personBlockCount = 0
	
	# Iterate over all combinations to create all possible pairings
	allSeatingCombinations = list(itertools.permutations(list(range(numberOfGuests))))
	allPossiblePairings = []
	for currCombination in allSeatingCombinations:
		allPairings = []
		for i in range(numberOfGuests):
			if i+1 >= numberOfGuests:
				allPairings.append([currCombination[i], currCombination[0]])
				allPairings.append([currCombination[i], currCombination[i-1]])
			elif i == 0:
				allPairings.append([currCombination[i], currCombination[i+1]])
				allPairings.append([currCombination[i], currCombination[numberOfGuests-1]])
			else:
				allPairings.append([currCombination[i], currCombination[i+1]])
				allPairings.append([currCombination[i], currCombination[i-1]])
		allPossiblePairings.append(allPairings)

	# Iterate over all pairings and find the maximum happiness
	maxHappiness = 0
	for currSetOfPairings in allPossiblePairings:
		currHappiness = 0
		for currPairing in currSetOfPairings:
			currHappiness += guestMatrix[currPairing[0]][currPairing[1]]
		if currHappiness > maxHappiness:
			maxHappiness = currHappiness
			maxPairing = currSetOfPairings
	
	# Print the result
	print('The maximal happiness for the optimal seating arrangement is given by {}.\nThe pairings are given as follows:'.format(maxHappiness))
	print(maxPairing)

	sys.exit()
