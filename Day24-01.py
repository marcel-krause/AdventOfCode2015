#!/usr/bin/env python
#Filename: Day24-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       09.01.2021                                                                                      #
#   Copyright:  Copyright (C) 2021, Marcel Krause                                                               #
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
from itertools import combinations
from math import prod


#------------------------------#
#          Functions           #
#------------------------------#
# lst: list of integers, N: integer, targetSum: integer. Creates all possible combinations of length N of instances in lst which sum up to targetSum.
def getCombinationsWithSum(lst, N, targetSum):
	return [numbers for numbers in combinations(lst, N) if sum(numbers)==targetSum]


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 24 - Riddle 01         |
|                                    |
+------------------------------------+
	''')

	# Read the input
	with open('Day24-01_input.dat', 'r', encoding='utf-8') as content_file:
		numbers = []
		for currLine in content_file.readlines():
			numbers.append(int(currLine.strip()))
		numbers
	
	# Define the target sum for each of the three packages
	targetSum = sum(numbers)//3

	# Create the package combination for the first group, which should contain the lowest number of elements j
	validCombinationsFound = False
	validFirstCombinations = []
	for j in range(2, len(numbers)-2):
		# If at least one possible package combination for each of the three groups was found in the previous iteration, we end our search
		if len(validFirstCombinations) > 0:
			break

		allCombinationsFirstGroup = getCombinationsWithSum(numbers, j, targetSum)
		validFirstCombinations = []
		if len(allCombinationsFirstGroup) == 0:
			continue
		else:
			# Iterate over all valid combinations for the first group
			for currCombination in allCombinationsFirstGroup:
				validCombinationsFound = False
				# Generate a new list with packages that were not used in group 1
				residualNumbers = [item for item in numbers if item not in list(currCombination)]
				# Iterate over all possible amounts of packages in the second group
				for i in range(1, len(residualNumbers)-1):
					if validCombinationsFound:
						break
					
					# Get the valid combinations for the second group with amount of packages i
					allCombinationsSecondGroup = getCombinationsWithSum(residualNumbers, i, targetSum)
					if len(allCombinationsSecondGroup) == 0:
						continue
					# Iterate over all valid combinations for the second group
					for currSecondCombination in allCombinationsSecondGroup:
						# The last group contains all remaining packages; if the sum of this list is equal to the target sum, we have found at least one valid combination for each of the three groups
						residualNumbersLast = [item for item in residualNumbers if item not in list(currSecondCombination)]
						if len(residualNumbersLast) == 0:
							continue
						elif sum(residualNumbersLast) == targetSum and list(currCombination) not in validFirstCombinations:
							validFirstCombinations.append(list(currCombination))
							validCombinationsFound = True
							break

	# Calculate the quantum entanglements of all valid first combinations
	entanglements = [prod(lst) for lst in validFirstCombinations]
	print('The ideal package configuration for the first group has QE={}.'.format(min(entanglements)))

	sys.exit()
