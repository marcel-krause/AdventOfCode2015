#!/usr/bin/env python
#Filename: Day05-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       11.01.2021                                                                                      #
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
|         Day 05 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Read the input file
	niceCount = 0
	with open('Day05-01_input.dat', 'r') as content_file:
		allLines = [line.rstrip('\n') for line in content_file]
		for currLine in allLines:
			isNiceDoublestructure = False
			isNiceDoublechar = False

			# Check for a pair of any two letters that appears at least twice in the string without overlapping
			regexDoublestructure = re.search(r'(\S{2,})(?=.*\1)', currLine)
			if regexDoublestructure:
				isNiceDoublestructure = True

			# Check for at least one letter which repeats with exactly one letter between them
			regexDoublechar = re.search(r'(\S{1,1})(?=[a-z]\1)', currLine)
			if regexDoublechar:
				isNiceDoublechar = True

			# Only if the current word passes all filters, we consider it to be "nice"
			if isNiceDoublestructure and isNiceDoublechar:
				niceCount += 1

	print(niceCount)

	sys.exit()
