#!/usr/bin/env python
#Filename: Day11-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       19.01.2019                                                                                      #
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
|         Day 11 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Some characters are forbidden
	forbiddenChars = ['i', 'l', 'o']

	# We start with the previous password as input, convert the chars to int values and iterate through all candidates to find the next password
	input = "hepxcrrq"
	candidate = [ord(input[0]), ord(input[1]), ord(input[2]), ord(input[3]), ord(input[4]), ord(input[5]), ord(input[6]), ord(input[7])]
	isStart = True
	passCounter = 0
	c1 = 97
	while c1 in range(97, 123):
		c2 = 97
		while c2 in range(97, 123):
			c3 = 97
			while c3 in range(97, 123):
				c4 = 97
				while c4 in range(97, 123):
					c5 = 97
					while c5 in range(97, 123):
						c6 = 97
						while c6 in range(97, 123):
							c7 = 97
							while c7 in range(97, 123):
								c8 = 97
								while c8 in range(97, 123):
									# Set the starting configuration to the input
									if isStart:
										c1 = ord(input[0])
										c2 = ord(input[1])
										c3 = ord(input[2])
										c4 = ord(input[3])
										c5 = ord(input[4])
										c6 = ord(input[5])
										c7 = ord(input[6])
										c8 = ord(input[7])
										isStart = False
										c8 += 1
										continue
									
									# Check if the current candidate contains forbidden characters and if so, skip the candidate
									tempCandidate = [c1, c2, c3, c4, c5, c6, c7, c8]
									if (ord(forbiddenChars[0]) in tempCandidate) or (ord(forbiddenChars[1]) in tempCandidate) or (ord(forbiddenChars[2]) in tempCandidate):
										c8 += 1
										continue

									# print(tempCandidate)
									# Check for an increasing line of at least three letters
									hasIncreasingLine = False
									for x in range(0, len(input)-2):
										if (tempCandidate[x+1] - tempCandidate[x] == 1) and (tempCandidate[x+2] - tempCandidate[x+1] == 1):
											hasIncreasingLine = True
									if not hasIncreasingLine:
										c8 += 1
										continue
									
									# Check whether the candidate has at least two pairs of same letters
									currString = chr(c1) + chr(c2) + chr(c3) + chr(c4) + chr(c5) + chr(c6) + chr(c7) + chr(c8)
									regexVowelcount = re.findall(r'(\w)\1+', currString)
									if not regexVowelcount or len(regexVowelcount) < 2:
										c8 += 1
										continue

									# If a candidate passed all checks, it is the next valid password, but we search for the next-to-next one
									passCounter += 1
									if passCounter > 1:
										print(currString)
										sys.exit()
									c8 += 1
								c7 += 1
							c6 += 1
						c5 += 1
					c4 += 1
				c3 += 1
			c2 += 1
		c1 += 1
	
	sys.exit()
