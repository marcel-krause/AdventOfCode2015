#!/usr/bin/env python
#Filename: Day23-01.py

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


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 23 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Read the input
	with open('Day23-01_input.dat', 'r', encoding='utf-8') as content_file:
		instructions = []
		for currLine in content_file.readlines():
			instructions.append(currLine.strip())

	# Set up the registers
	register = {
		'a': 1,
		'b': 0
	}
	
	# Iterate through all instructions
	currInstrIdx = 0
	while True:
		# Exit condition
		if currInstrIdx < 0 or currInstrIdx >= len(instructions):
			break
		
		# Get the current instruction
		currInstr = instructions[currInstrIdx]

		# Perform the instruction
		if 'hlf' in currInstr:
			register[currInstr.split(' ')[1]] = register[currInstr.split(' ')[1]]//2
			currInstrIdx += 1
		elif 'tpl' in currInstr:
			register[currInstr.split(' ')[1]] = int(register[currInstr.split(' ')[1]]*3)
			currInstrIdx += 1
		elif 'inc' in currInstr:
			register[currInstr.split(' ')[1]] = int(register[currInstr.split(' ')[1]] + 1)
			currInstrIdx += 1
		elif 'jmp' in currInstr:
			if '+' in currInstr:
				currInstrIdx += int(currInstr.split('+')[1])
			elif '-' in currInstr:
				currInstrIdx -= int(currInstr.split('-')[1])
		elif 'jie' in currInstr:
			tmp = currInstr.split(', ')
			if register[tmp[0].split(' ')[1]]%2 == 0:
				if '+' in currInstr:
					currInstrIdx += int(tmp[1].replace('+', ''))
				elif '-' in currInstr:
					currInstrIdx -= int(tmp[1].replace('-', ''))
			else:
				currInstrIdx += 1
		elif 'jio' in currInstr:
			tmp = currInstr.split(', ')
			if register[tmp[0].split(' ')[1]] == 1:
				if '+' in currInstr:
					currInstrIdx += int(tmp[1].replace('+', ''))
				elif '-' in currInstr:
					currInstrIdx -= int(tmp[1].replace('-', ''))
			else:
				currInstrIdx += 1
		
	print('The value of register b after termination of the progam is {}.'.format(register['b']))

	sys.exit()
