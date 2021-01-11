#!/usr/bin/env python
#Filename: Day20-02.py

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
from math import floor


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 20 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Get the input
	targetNumPresents = 34000000

	# Iterate over the houses to check which house corresponds to the target number
	presentsInHouse = [0]*int(targetNumPresents/11+1)
	for elf in range(1, len(presentsInHouse)):
		visitCount = 0
		for house in range(elf, len(presentsInHouse), elf):
			if visitCount <= 50:
				presentsInHouse[house-1] += 11*elf
				visitCount += 1
			else:
				break
	
	for house in range(1, len(presentsInHouse)):
		if presentsInHouse[house-1] > targetNumPresents:
			break
	
	print('House number {} receives {} presents and is hence the first to receive at least {} presents.'.format(house, presentsInHouse[house-1], targetNumPresents))

	sys.exit()
