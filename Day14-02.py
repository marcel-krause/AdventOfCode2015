#!/usr/bin/env python
#Filename: Day14-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       28.01.2020                                                                                      #
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
#          Classes           #
#----------------------------#
class Reindeer:
	def __init__(self, name, speed, speedTime, restTime):
		self.name = name
		self.speed = speed
		self.speedTime = speedTime
		self.restTime = restTime
		self.currSpeedTime = 0
		self.currRestTime = restTime
		self.score = 0
		self.traveledDistance = 0

	def updateDistance(self):
		# At this point, the reindeer has to rest in the following rounds
		if self.currSpeedTime == self.speedTime:
			self.currRestTime -= 1
			if self.currRestTime == 0:
				self.currRestTime = self.restTime
				self.currSpeedTime = 0
		# At this point, the reindeer travels for one second
		else:
			self.currSpeedTime += 1
			self.traveledDistance += self.speed
		

#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 14 - Riddle 02         |
|                                    |
+------------------------------------+
	''')

	# Specify the total travel time
	travelTime = 2503

	# Read the input
	with open('Day14-01_input.dat', 'r', encoding='utf-8') as content_file:
		data = (content_file.readlines())
		reindeers = []
		for currLine in data:
			reindeerName = currLine.split(' ')[0]
			reindeerStats = re.findall(r'\d+', currLine)
			reindeers.append(Reindeer(reindeerName, int(reindeerStats[0]), int(reindeerStats[1]), int(reindeerStats[2])))

	# Calculate the distances traveled
	maxScore = 0
	for i in range(1, travelTime+1):
		maxDistance = 0
		for currReindeer in reindeers:
			currReindeer.updateDistance()
			if currReindeer.traveledDistance > maxDistance:
				maxDistance = currReindeer.traveledDistance
		for currReindeer in reindeers:
			if currReindeer.traveledDistance == maxDistance:
				currReindeer.score += 1
			if currReindeer.score > maxScore:
				maxScore = currReindeer.score
	
	# Print the result
	print('The winning reindeer has a score of {}.'.format(maxScore))

	sys.exit()
