#!/usr/bin/env python
#Filename: Day10-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       14.01.2019                                                                                      #
#   Copyright:  Copyright (C) 2019, Marcel Krause                                                               #
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
# import re
# import numpy as np
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
def getNewValue(oldVal):
	newString = ""
	while True:
		counter = 1
		while True:
			currChar = oldVal[:1]
			if len(oldVal) == 1:
				newString += str(counter) + currChar
				return(newString)
			else:
				oldVal = oldVal[1:]
			if currChar == oldVal[:1]:
				counter += 1
			else:
				newString += str(counter) + currChar
				break

#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 10 - Riddle 01         |
|                                    |
+------------------------------------+
	''')

	# Get the input and determine the number of iterations
	input = "1321131112"
	iterations = 40

	# Generate the Conway sequence
	print(len(input))
	for x in range(0, iterations):
		input = getNewValue(input)
		print(len(input))
	
	sys.exit()
