#!/usr/bin/env python
#Filename: Day20-01.py

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
from sympy.ntheory import factorint


#------------------------------#
#          Functions           #
#------------------------------#
# Calculates the divisor function for the number n by means of the prime factors of n, using Eq. (14) from https://mathworld.wolfram.com/DivisorFunction.html
def divisorFunction(n):
	primeFactors = factorint(n)
	prod = 1
	for p, alpha in primeFactors.items():
		prod *= (p**(alpha+1) - 1)/(p-1)
	return int(prod)


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 20 - Riddle 01         |
|                                    |
+------------------------------------+
	''')

	# Get the input
	targetNumPresents = 34000000

	# Iterate over the houses to check which house corresponds to the target number
	i = 2
	while True:
		numPresents = 10*divisorFunction(i)
		if numPresents >= targetNumPresents:
			break
		i += 1
	print('House number {} receives {} presents and is hence the first to receive at least {} presents.'.format(i, numPresents, targetNumPresents))

	sys.exit()
