#!/usr/bin/env python
#Filename: Day19-02.py

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
|         Day 19 - Riddle 02         |
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
				if currLine.split(' => ')[1].strip() not in moleculeReplacements.keys():
					moleculeReplacements[currLine.split(' => ')[1].strip()] = currLine.split(' => ')[0].strip()
			else:
				targetMolecule = currLine.strip()

	# Perform all possible replacements
	currMolecule = targetMolecule
	print('Step 0 ...')
	print(currMolecule)
	steps = 1
	while True:
		for molecule, replacement in moleculeReplacements.items():
			newMolecule = currMolecule.replace(molecule, replacement, 1)
			if replacement == 'e' and newMolecule == 'e':
				print('\nStep {} ...'.format(steps))
				currMolecule = newMolecule
				print(currMolecule)
				print('\nTarget molecule is created in {} steps.'.format(steps))
				sys.exit()
			if replacement == 'e' and newMolecule != 'e':
				continue
			if newMolecule != currMolecule:
				print('\nStep {} ...'.format(steps))
				currMolecule = newMolecule
				print(currMolecule)
				steps += 1
				break

	sys.exit()
