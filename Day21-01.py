#!/usr/bin/env python
#Filename: Day21-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       29.12.2020                                                                                      #
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
from math import ceil
from itertools import combinations


#------------------------------#
#          Functions           #
#------------------------------#
# Calculates the winner in a battle between player and opponent, given each of the two players' stats. Returns True if the player wins and False otherwise.
# The winner is easily determined by finding the roots of the two linear equations which represent the hit points of each player.
# Since the player hits first, it suffices that the round which corresponds to the root of the linear equation for the player is higher *or equal* to the round for the opponent.
def calcWinner(playerStats, opponentStats):
	deltaHitPlayer = opponentStats['damage'] - playerStats['armor'] if opponentStats['damage'] - playerStats['armor'] > 0 else 1
	deltaHitOpponent = playerStats['damage'] - opponentStats['armor'] if playerStats['damage'] - opponentStats['armor'] > 0 else 1
	playerRoot = ceil(playerStats['hitpoints']/deltaHitPlayer)
	opponentRoot = ceil(opponentStats['hitpoints']/deltaHitOpponent)
	return True if playerRoot >= opponentRoot else False


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 21 - Riddle 01         |
|                                    |
+------------------------------------+
	''')

	# Get the input
	with open('Day21-01_input.dat', 'r', encoding='utf-8') as content_file:
		opponentStats = {}
		for currLine in content_file.readlines():
			if 'Hit Points' in currLine:
				opponentStats['hitpoints'] = int(currLine.strip().split(': ')[1])
			if 'Damage' in currLine:
				opponentStats['damage'] = int(currLine.strip().split(': ')[1])
			if 'Armor' in currLine:
				opponentStats['armor'] = int(currLine.strip().split(': ')[1])
	
	# Get the shop content
	with open('Day21-01_input2.dat', 'r', encoding='utf-8') as content_file:
		shop = {}
		for currLine in content_file.readlines():
			# Skip empty lins
			if currLine.strip() == '':
				continue
			# Sort the type of armory block
			if 'Weapons:' in currLine or 'Armor:' in currLine or 'Rings:' in currLine:
				currBlock = currLine.split(':')[0]
				shop[currBlock] = []
				continue
			# Add each item to the corresponding block
			splittedLine = currLine.strip().split()
			itemName = splittedLine[0] if '+' not in currLine else ' '.join(splittedLine[:2])
			item = {
				'name': itemName,
				'cost': int(splittedLine[-3]),
				'damage': int(splittedLine[-2]),
				'armor': int(splittedLine[-1])
			}
			shop[currBlock].append(item)
	
	# Define the player's starting stats
	playerStats = {
		'hitpoints': 100,
		'damage': 0,
		'armor': 0
	}

	# Get all possible ring combinations
	allRingCombinations = list(combinations(range(len(shop['Rings'])), 1)) + list(combinations(range(len(shop['Rings'])), 2))

	# Define the lowest cost of the winning configuration
	winningCost = float('inf')

	# The player needs one weapon, so we iterate over all of them
	for i in range(len(shop['Weapons'])):
		
		# Iterate over all armory (-1 indicates that we do not take an armory piece since it's optional)
		for j in range(-1, len(shop['Armor'])):
			
			# Iterate over all one ring combinations
			for k in range(-1, len(allRingCombinations)):
				currPlayerStats = playerStats.copy()
				currRingConfig = ''
				currRingCost = 0
				currRingDamage = 0
				currRingArmor = 0
				if k >= 0:
					for m in allRingCombinations[k]:
						currRingConfig += shop['Rings'][m]['name'] + ', '
						currRingCost += shop['Rings'][m]['cost']
						currRingDamage += shop['Rings'][m]['damage']
						currRingArmor += shop['Rings'][m]['armor']
					currRingConfig.strip(', ')

				# Add all item values together
				currConfigName = shop['Weapons'][i]['name']
				currCost = shop['Weapons'][i]['cost']
				currDamage = shop['Weapons'][i]['damage']
				currArmor = shop['Weapons'][i]['armor']
				if j >= 0:
					currConfigName += ', ' + shop['Armor'][j]['name']
					currCost += shop['Armor'][j]['cost']
					currDamage += shop['Armor'][j]['damage']
					currArmor += shop['Armor'][j]['armor']
				currConfigName += ', ' + currRingConfig
				currCost += currRingCost
				currDamage += currRingDamage
				currArmor += currRingArmor
				currConfigName = currConfigName.strip().strip(',')

				currPlayerStats['damage'] = currDamage
				currPlayerStats['armor'] = currArmor

				# Calculate the winner and update the cost of the winning configuration if it is smaller than the current lowest value
				if calcWinner(currPlayerStats, opponentStats):
					if currCost < winningCost:
						winningCost = currCost
						winningConfigName = currConfigName
						winningConfig = currPlayerStats.copy()

	print('The least amount of gold required for winning is given by {}.'.format(winningCost))

	sys.exit()
