#!/usr/bin/env python
#Filename: Day12-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       20.01.2019                                                                                      #
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
import json
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
|         Day 12 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Read the input
	with open('Day12-01_input.dat', 'r', encoding='utf-8') as content_file:
		data = json.load(content_file)

		currObject = data
		currIndices = list(data)
		# for currIndex in currIndices:
		# 	print(json.dumps(data[currIndex], sort_keys=False, indent=2))
		print(json.dumps(data["c"], sort_keys=False, indent=2))
		
		# print(json.dumps(data, sort_keys=False, indent=2))
		# print()

	sys.exit()
