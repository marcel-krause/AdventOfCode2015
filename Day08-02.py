#!/usr/bin/env python
#Filename: Day08-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       02.01.2019                                                                                      #
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
import re
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


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 08 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Read the input file
	with open('Day08-01_input.dat', 'r', encoding='utf-8') as content_file:
		allLines = [line.rstrip('\n') for line in content_file]

	# Read the number of code characters
	codeChars = 0
	newCodeChars = 0
	targetString = ""
	for currLine in allLines:
		codeChars += len(currLine)
		tempString = currLine
		tempString = tempString.replace('\\', '\\\\').replace('\"', '\\\"')
		tempString = '\"' + tempString + '\"'
		targetString += currLine + '\n' + tempString + '\n' + str(len(tempString)) + "-" + str(len(currLine)) + "=" + str(len(tempString) - len(currLine)) + '\n\n'
		newCodeChars += len(tempString)

	print(newCodeChars-codeChars)
	
	sys.exit()
