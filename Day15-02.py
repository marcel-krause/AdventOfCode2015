#!/usr/bin/env python
#Filename: Day15-02.py

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
def allIterations(maxIterations, currMax, stateVariable, numIterations, ingredientProperties):
	if numIterations-1 == 0:
		fullStateVariable = stateVariable + [maxIterations - sum(stateVariable)]
		calcRecipeValue(ingredientProperties, fullStateVariable)
	else:
		for i in range(0, maxIterations-currMax+1):
			allIterations(maxIterations, sum(stateVariable+[i]), stateVariable+[i], numIterations-1, ingredientProperties)

def calcRecipeValue(ingredientProperties, stateVariable):
	global maxRecipeVal
	recipeVal = 1
	for ingr, val in ingredientProperties.items():
		ingrSum = 0
		for i in range(len(val)):
			ingrSum += stateVariable[i]*val[i]
		if ingr == 'calories':
			if ingrSum == 500:
				ingrSum = 1
			else:
				ingrSum = 0
		if ingrSum < 0:
			ingrSum = 0
		recipeVal *= ingrSum
	if recipeVal > maxRecipeVal:
		maxRecipeVal = recipeVal


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 15 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Read the input
	ingredientList = []
	ingredientProperties = {}
	with open('Day15-01_input.dat', 'r', encoding='utf-8') as content_file:
		for currLine in content_file.readlines():
			ingredientList.append(currLine.split(': ')[0])
			for ingr in currLine.split(': ')[1].split(', '):
				if ingr.split(' ')[0] not in ingredientProperties.keys():
					ingredientProperties[ingr.split(' ')[0]] = [int(ingr.split(' ')[1])]
				else:
					ingredientProperties[ingr.split(' ')[0]].append(int(ingr.split(' ')[1]))

	# Calculate the maximum recipe value
	maxIngredientValue = 100
	numberOfIngredients = len(ingredientList)
	maxRecipeVal = 0
	allIterations(maxIngredientValue, 0, [], numberOfIngredients, ingredientProperties)

	# Print the result
	print("The maximum recipe value is {}.".format(maxRecipeVal))

	sys.exit()
