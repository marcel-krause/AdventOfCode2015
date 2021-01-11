#!/usr/bin/env python
#Filename: Day12-02.py

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
import json


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 12 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Read the input
	with open('Day12-01_input.dat', 'r', encoding='utf-8') as content_file:
		data = json.load(content_file)

		# print(json.dumps(currObject['e'], sort_keys=False, indent=2))
		allObjectsDone = False
		fullSum = 0

		currObjects = [data]

		while True:
			currSubObjectCollector = []
			
			for currObject in currObjects:
				currObjectSum = 0
				skipCurrObject = False

				# Discard the current object if it contains a value 'red'
				if isinstance(currObject, dict):
					for val in currObject.values():
						if val == 'red':
							skipCurrObject = True
				if not skipCurrObject:
					# If the current object is an integer, directly add it to the sum of integers
					if isinstance(currObject, int):
						currObjectSum += currObject
					
					# If the current object is a list, traverse through the list and add up integers that are in the list; add sub-lists and dicts to another list for the next iteration
					if isinstance(currObject, list):
						for val in currObject:
							if isinstance(val, int):
								currObjectSum += val
							elif isinstance(val, dict) or isinstance(val, list):
								currSubObjectCollector.append(val)
					
					# If the current object is a list, traverse through the list and add up integers that are in the list; add sub-lists and dicts to another list for the next iteration
					if isinstance(currObject, dict):
						for val in currObject.values():
							if isinstance(val, int):
								currObjectSum += val
							elif isinstance(val, dict) or isinstance(val, list):
								currSubObjectCollector.append(val)
					
					# Add the object sum to the overall sum
					fullSum += currObjectSum

			# In case no sub-lists or dicts were found, we are done
			if len(currSubObjectCollector) == 0:
				break
			else:
				currObjects = currSubObjectCollector
		
		print('The sum of all relevant items is given by {}.'.format(fullSum))

	sys.exit()
