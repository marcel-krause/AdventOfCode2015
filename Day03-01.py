#!/usr/bin/env python
#Filename: Day03-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       27.12.2018                                                                                      #
#   Copyright:  Copyright (C) 2018, Marcel Krause                                                               #
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
# import os
# from shutil import copyfile, rmtree
# from math import pi, sqrt
# import random
# import subprocess

#------------------------------#
#           Settings           #
#------------------------------#


#------------------------------#
#          Functions           #
#------------------------------#


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 03 - Riddle 01         |
|                                    |
+------------------------------------+
	''')

	# Read the input file
	x = 0
	y = 0
	visitedHouses = {
		"0,0": 1
	}
	with open('Day03-01_input.dat', 'r') as content_file:
		while True:
			inString = content_file.read(1)
			if not inString:
				break
			if inString is ">":
				x += 1
			elif inString is "<":
				x -= 1
			elif inString is "v":
				y -= 1
			elif inString is "^":
				y += 1
			if str(x) + "," + str(y) in visitedHouses:
				visitedHouses[str(x) + "," + str(y)] += 1
			else:
				visitedHouses[str(x) + "," + str(y)] = 1
	print(len(visitedHouses))

	sys.exit()
