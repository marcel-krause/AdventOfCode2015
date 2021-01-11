#!/usr/bin/env python
#Filename: Day16-01.py

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
|         Day 16 - Riddle 01         |
|                                    |
+------------------------------------+
	''')

	# Specify the 'target Sue'
	targetSue = {
		'children': 3,
		'cats': 7,
		'samoyeds': 2,
		'pomeranians': 3,
		'akitas': 0,
		'vizslas': 0,
		'goldfish': 5,
		'trees': 3,
		'cars': 2,
		'perfumes': 1
	}

	# Read the input
	with open('Day16-01_input.dat', 'r', encoding='utf-8') as content_file:
		data = (content_file.readlines())
		currSueNumber = 1
		for currLine in data:
			# Specify the prototype Sue
			currSue = {
				'children': None,
				'cats': None,
				'samoyeds': None,
				'pomeranians': None,
				'akitas': None,
				'vizslas': None,
				'goldfish': None,
				'trees': None,
				'cars': None,
				'perfumes': None
			}
			# Get the info about the current Sue
			currSueNumber = int((currLine.split('Sue ')[1]).split(':')[0])
			currSueInfo = ': '.join(currLine.split(': ')[1:])
			for currInfo in currSueInfo.split(', '):
				currSue[currInfo.split(': ')[0]] = int(currInfo.split(': ')[1])

			# Filter out the Sue's which are not correct
			sueCandidate = True
			for currSueInfo in currSue:
				if currSue[currSueInfo] is not None:
					if currSue[currSueInfo] != targetSue[currSueInfo]:
						sueCandidate = False
			if not sueCandidate:
				continue
			print('Aunt Sue number {} sent the gift.'.format(currSueNumber))

	sys.exit()
