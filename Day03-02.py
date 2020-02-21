#!/usr/bin/env python
#Filename: Day03-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       28.12.2018                                                                                      #
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
|         Day 03 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Read the input file
	x = [0, 0]
	y = [0, 0]
	visitedHouses = {
		"0,0": 2
	}
	endOfFile = False
	with open('Day03-01_input.dat', 'r') as content_file:
		while True:
			for c in range(0,2):
				inString = content_file.read(1)
				if not inString:
					endOfFile = True
					break
				if inString is ">":
					x[c] += 1
				elif inString is "<":
					x[c] -= 1
				elif inString is "v":
					y[c] -= 1
				elif inString is "^":
					y[c] += 1
				if str(x[c]) + "," + str(y[c]) in visitedHouses:
					visitedHouses[str(x[c]) + "," + str(y[c])] += 1
				else:
					visitedHouses[str(x[c]) + "," + str(y[c])] = 1
			if endOfFile:
				break
	print(len(visitedHouses))

	sys.exit()
