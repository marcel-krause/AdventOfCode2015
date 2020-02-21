#!/usr/bin/env python
#Filename: Day07-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       30.12.2018                                                                                      #
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
import re
import numpy as np
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
|         Day 07 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Read the input file
	with open('Day07-02_input.dat', 'r') as content_file:
		allLines = [line.rstrip('\n') for line in content_file]

	mapping = []

	while True:
		deleteIndices = []

		# Search for direct value assignments to the wires
		for x in range(0,len(allLines)):
			regSearch = re.findall(r'^(\d+) -> (\w+)$', allLines[x])
			if regSearch:
				mapping.append((regSearch[0][1], regSearch[0][0]))
				deleteIndices.append(x)

		# Search for complement assignments
		for x in range(0,len(allLines)):
			regSearch = re.findall(r'^NOT (\d+) -> (\w+)$', allLines[x])
			if regSearch:
				mapping.append((regSearch[0][1], str(65536 + (~ int(regSearch[0][0])))))
				deleteIndices.append(x)

		# Search for AND gates
		for x in range(0,len(allLines)):
			regSearch = re.findall(r'^(\d+) AND (\d+) -> (\w+)$', allLines[x])
			if regSearch:
				mapping.append((regSearch[0][2], str(int(regSearch[0][0]) & int(regSearch[0][1]))))
				deleteIndices.append(x)

		# Search for OR gates
		for x in range(0,len(allLines)):
			regSearch = re.findall(r'^(\d+) OR (\d+) -> (\w+)$', allLines[x])
			if regSearch:
				mapping.append((regSearch[0][2], str(int(regSearch[0][0]) | int(regSearch[0][1]))))
				deleteIndices.append(x)

		# Search for left shifts
		for x in range(0,len(allLines)):
			regSearch = re.findall(r'^(\d+) LSHIFT (\d+) -> (\w+)$', allLines[x])
			if regSearch:
				mapping.append((regSearch[0][2], str(int(regSearch[0][0]) << int(regSearch[0][1]))))
				deleteIndices.append(x)

		# Search for right shifts
		for x in range(0,len(allLines)):
			regSearch = re.findall(r'^(\d+) RSHIFT (\d+) -> (\w+)$', allLines[x])
			if regSearch:
				mapping.append((regSearch[0][2], str(int(regSearch[0][0]) >> int(regSearch[0][1]))))
				deleteIndices.append(x)

		# Sort the deletion indices in descending order so that del can be applied directly
		deleteIndices.sort(reverse=True)
		
		# Replace the missing values with the found ones
		for x in range(0,len(allLines)):
			splitString = allLines[x].split(" ")
			newString = ""
			for y in range(0, len(splitString)):
				for k, v in mapping:
					if splitString[y] == k:
						splitString[y] = v
				newString += " " + splitString[y]
			newString = newString.strip()
			allLines[x] = newString

		# Delete "completed" instructions from the instruction list
		for deleteIndex in deleteIndices:
			del allLines[deleteIndex]
		
		# If the source list is empty, we are done
		if len(allLines) == 0:
			break

	# Print the value for wire 'a':
	for k, v in mapping:
		if k == 'a':
			print(v)
	
	sys.exit()
