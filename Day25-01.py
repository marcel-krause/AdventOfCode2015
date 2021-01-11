#!/usr/bin/env python
#Filename: Day25-01.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       08.01.2020                                                                                      #
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


#------------------------------#
#          Functions           #
#------------------------------#
# n, m: integers. Calculates the figurative triangle-related number at position with row n and column m
def getFigurativeNumber(n, m):
	return int((n+m)**2/2 - (m+3*n)/2 + 1)

# x: integer. Calculates the code at the wanted id x
def calcCode(x):
	prevCode = 20151125
	multiplicator = 252533
	divisor = 33554393
	if x == 1:
		return prevCode
	for _ in range(1, x):
		prevCode = (prevCode*multiplicator)%divisor
	return prevCode


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 25 - Riddle 01         |
|                                    |
+------------------------------------+
	''')

	# Get the input
	row = 3010
	col = 3019
	
	wantedCodeId = getFigurativeNumber(row, col)
	currCode = calcCode(wantedCodeId)

	print('Your code at row {} and col {} is given as {}.'.format(row, col, currCode))

	sys.exit()
