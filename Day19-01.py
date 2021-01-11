#!/usr/bin/env python
#Filename: Day19-01.py

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
|         Day 19 - Riddle 01         |
|                                    |
+------------------------------------+
	''')

	# Read the input
	with open('Day19-01_input.dat', 'r', encoding='utf-8') as content_file:
		moleculeReplacements = {}
		for currLine in content_file.readlines():
			if currLine.strip() == '':
				continue
			if '=>' in currLine:
				if currLine.split(' => ')[0] not in moleculeReplacements.keys():
					moleculeReplacements[currLine.split(' => ')[0]] = [currLine.split(' => ')[1].strip()]
				else:
					moleculeReplacements[currLine.split(' => ')[0]].append(currLine.split(' => ')[1].strip())
			else:
				calibrationPoint = currLine.strip()

	# Perform all possible replacements
	alDistinctReplacements = []
	for molecule, replacements in moleculeReplacements.items():
		moleculeSplit = calibrationPoint.split(molecule)
		for replacement in replacements:
			for i in range(len(moleculeSplit)-1):
				replacedString = ''
				for j in range(len(moleculeSplit)):
					if i == j:
						replacedString += moleculeSplit[j] + replacement
					elif j == len(moleculeSplit)-1:
						replacedString += moleculeSplit[j]
					else:
						replacedString += moleculeSplit[j] + molecule
				if replacedString not in alDistinctReplacements:
					alDistinctReplacements.append(replacedString)
	print('There are {} distinct replacements.'.format(len(alDistinctReplacements)))

	sys.exit()
