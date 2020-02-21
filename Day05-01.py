#!/usr/bin/env python
#Filename: Day05-01.py

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
|         Day 05 - Riddle 01         |
|                                    |
+------------------------------------+
	''')

	# Read the input file
	niceCount = 0
	with open('Day05-01_input.dat', 'r') as content_file:
		allLines = [line.rstrip('\n') for line in content_file]
		for currLine in allLines:
			isNiceVowelcount = False
			isNiceForbiddenwords = False
			isNiceEqualletters = False


			# Solution using regular expressions for pattern matching

			# Check for the vowel count (contains at least three vowels)
			regexVowelcount = re.findall(r'[aeiou]', currLine)
			if regexVowelcount and len(regexVowelcount) >= 3:
				isNiceVowelcount = True

			# Check if no forbidden words are contained
			regexForbiddenwords = re.search(r'(ab)|(cd)|(pq)|(xy)', currLine)
			if not regexForbiddenwords:
				isNiceForbiddenwords = True

			# Check if there are at least two equal letters appearing in a row
			regexEqualletters = re.search(r'(\w)\1+', currLine)
			if regexEqualletters:
				isNiceEqualletters = True


			# Alternate version using "manual" pattern matching below

			# # Check for the vowel count (contains at least three vowels)
			# countA = currLine.count('a')
			# countE = currLine.count('e')
			# countI = currLine.count('i')
			# countO = currLine.count('o')
			# countU = currLine.count('u')
			# vowelCount = countA + countE + countI + countO + countU
			# if vowelCount >= 3:
			# 	isNiceVowelcount = True
			
			# # Check if no forbidden words are contained
			# if ("ab" not in currLine) and ("cd" not in currLine) and ("pq" not in currLine) and ("xy" not in currLine):
			# 	isNiceForbiddenwords = True
			
			# # Check if there are at least two equal letters appearing in a row
			# formerC = ""
			# for c in currLine:
			# 	if c is formerC:
			# 		isNiceEqualletters = True
			# 	formerC = c

			# Only if the current word passes all filters, we consider it to be "nice"
			if isNiceVowelcount and isNiceForbiddenwords and isNiceEqualletters:
				niceCount += 1

	print(niceCount)

	sys.exit()
