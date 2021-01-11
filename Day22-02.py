#!/usr/bin/env python
#Filename: Day22-02.py

 ###############################################################################################################
#                                                                                                               #
#                               Advent of Code 2015 - Solutions of Problems                                     #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       29.12.2020                                                                                      #
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


#------------------------------#
#           Settings           #
#------------------------------#
hardmodeActive = True		# Boolean. Whether hard mode (i.e. the Player takes 1HP damage at the beginning of every Player's turn) is active or not. Default: True


#------------------------------#
#          Functions           #
#------------------------------#
def playGame(playerStats, opponentStats, castOrder, spellbook, hardmodeActive, verbose):
	# Get the lowest mana cost all all the spells in order to check whether the player has still enough mana to cast any spell
	lowestManaCost = float('inf')
	for spell in spellbook.values():
		if spell['cost'] < lowestManaCost:
			lowestManaCost = spell['cost']

	# State variable for active effects, all cast spells and total mana spent
	activeEffects = {}
	castSpells = []
	totalManaCosts = 0

	# Play rounds
	playersTurn = True
	turnCount = 1
	currPlayerStats = playerStats.copy()
	currOpponentStats = opponentStats.copy()
	castRound = 0
	while True:
		# Check if shield wore off
		if 'Shield' in activeEffects:
			currPlayerStats['Armor'] = spellbook['Shield']['armorMe']
		else:
			currPlayerStats['Armor'] = 0

		# Console output
		if verbose:
			currPlayersName = 'Player' if playersTurn else 'Boss'
			playerAdditionalString = ' - ' if 'Shield' in activeEffects.keys() or 'Recharge' in activeEffects.keys() else ''
			playerAdditionalString += 'Shielded ({}/{}), '.format(spellbook['Shield']['lastsTurns'] - activeEffects['Shield'] + 1, spellbook['Shield']['lastsTurns']) if 'Shield' in activeEffects.keys() else ''
			playerAdditionalString += 'Recharging ({}/{}), '.format(spellbook['Recharge']['lastsTurns'] - activeEffects['Recharge'] + 1, spellbook['Recharge']['lastsTurns']) if 'Recharge' in activeEffects.keys() else ''
			playerAdditionalString = ' ' + playerAdditionalString.strip(', ')
			opponentAdditionalString = ' - Poisoned ({}/{})'.format(spellbook['Poison']['lastsTurns'] - activeEffects['Poison'] + 1, spellbook['Poison']['lastsTurns']) if 'Poison' in activeEffects.keys() else ''
			print('-- {} turn --'.format(currPlayersName))
			print(' Player ( {} HP | {} Armor | {} Mana )'.format(currPlayerStats['HP'], currPlayerStats['Armor'], currPlayerStats['Mana']) + playerAdditionalString)
			print(' vs. Boss ( {} HP | {} Damage )'.format(currOpponentStats['HP'], currOpponentStats['Damage']) + opponentAdditionalString)
		
		# Account for the hard mode effect
		if playersTurn and hardmodeActive:
			if verbose:
				print('The Player is engulfed in the Dark Aura of the Boss. Player takes 1HP damage.')
			if currPlayerStats['HP'] - 1 <= 0:
				playerKilled = True
				if verbose:
					print('This kills the Player. Boss has won!')
				break
			else:
				currPlayerStats['HP'] -= 1
		
		# Account for all active effects
		newActiveEffects = activeEffects.copy()
		opponentKilled = False
		for eff, roundCounter in activeEffects.items():
			# Apply the effects
			if eff == 'Recharge':
				currPlayerStats['Mana'] += spellbook[eff]['rechargeMana']
				if verbose:
					print('{} provides {} Mana for Player.'.format(eff, spellbook[eff]['rechargeMana']))
			if eff == 'Poison':
				if verbose:
					print('{} deals {} damage to Boss.'.format(eff, spellbook[eff]['damageOpponent']))
				if currOpponentStats['HP'] - spellbook[eff]['damageOpponent'] <= 0:
					opponentKilled = True
					if verbose:
						print('This kills the Boss. Player has won!')
					break
				else:
					currOpponentStats['HP'] -= spellbook[eff]['damageOpponent']
			# Wear off the effects
			if activeEffects[eff]-1 == 0:
				additionalEffectInfo = 'Player\'s armor is reduced to 0 in the next turn.' if eff == 'Shield' else ''
				if verbose:
					print('{} wears off. {}'.format(eff, additionalEffectInfo))
				del newActiveEffects[eff]
			else:
				newActiveEffects[eff] = roundCounter - 1
		activeEffects = newActiveEffects.copy()
		if opponentKilled:
			break

		# Player attacks every second round with a spell
		if playersTurn:
			playerKilled = False
			# If there are no more spells in the castOrder, we consider the game to be unfinished
			if castRound >= len(castOrder):
				if verbose:
					print('The Player has not specified any further spell.')
					print('This ends the match. There is no winner!')
				break
		
			# If the Player does not have enough mana to cast even the cheapest spell, they lose
			if currPlayerStats['Mana'] < lowestManaCost:
				playerKilled = True
				if verbose:
					print('Player does not have enough Mana to cast any spell anymore.')
					print('This kills the Player. Boss has won!')
				break

			currSpell = castOrder[castRound]
			castRound += 1
			opponentKilled = False
	
			# If the Player does not have enough mana to cast the spell, the Player loses
			if currPlayerStats['Mana'] < spellbook[currSpell]['cost']:
				playerKilled = True
				if verbose:
					print('Player attempts to cast {}, but does not have enough Mana.'.format(currSpell))
					print('This kills the Player. Boss has won!')
				break
			else:
				# Account for effects
				effectAlreadyCast = False
				if spellbook[currSpell]['lastsTurns'] > 0:
					# Effects that are already activated cannot be cast again and if the Player tries, they die
					if currSpell in activeEffects.keys():
						effectAlreadyCast = True
						playerKilled = True
						if verbose:
							print('Player attempts to cast {}, but {} is still active.'.format(currSpell, currSpell))
							print('This kills the Player. Boss has won!')
						break
					else:
						activeEffects[currSpell] = spellbook[currSpell]['lastsTurns']
						additionalSpellInfo = '{}'.format(currSpell)
						if currSpell == 'Shield':
							additionalSpellInfo += ' increases the Player\'s armor by {} in the next turn and'.format(spellbook[currSpell]['armorMe'])
						additionalSpellInfo += ' lasts for {} turns.'.format(spellbook[currSpell]['lastsTurns'])

				# Otherwise, account for instant spells
				else:
					# Damage dealt to the boss
					if currOpponentStats['HP'] - spellbook[currSpell]['damageOpponent'] <= 0:
						opponentKilled = True
					else:
						currOpponentStats['HP'] -= spellbook[currSpell]['damageOpponent']

					# HP regenerated for the Player
					currPlayerStats['HP'] += spellbook[currSpell]['healingMe']

					# Formatting for console output
					if verbose:
						additionalSpellInfo = '{} deals {} damage to the Boss'.format(currSpell, spellbook[currSpell]['damageOpponent'])
						if spellbook[currSpell]['healingMe'] > 0:
							additionalSpellInfo += ' and heals the player by {} HP'.format(spellbook[currSpell]['healingMe'])
						additionalSpellInfo += '.'
				
				# Reduce the mana and account for the total mana cost
				if not effectAlreadyCast:
					currPlayerStats['Mana'] -= spellbook[currSpell]['cost']
					totalManaCosts += spellbook[currSpell]['cost']
					castSpells.append(currSpell)
					if verbose:
						print('Player casts {} for {} Mana. {}'.format(currSpell, spellbook[currSpell]['cost'], additionalSpellInfo))
				
				# Console output
				if opponentKilled:
					if verbose:
						print('This kills the Boss. Player has won!')
					break
		
		# Boss attacks every second round with only a basic attack
		if not playersTurn:
			bossResidualDamage = currOpponentStats['Damage']-currPlayerStats['Armor'] if currOpponentStats['Damage'] > currPlayerStats['Armor'] else 1
			playerKilled = False
			if currPlayerStats['HP'] - bossResidualDamage <= 0:
				playerKilled = True
			else:
				currPlayerStats['HP'] -= bossResidualDamage
			if verbose:
				bossAttackDamage = str(currOpponentStats['Damage']) if currPlayerStats['Armor']==0 else '{} - {} = {}'.format(currOpponentStats['Damage'], currPlayerStats['Armor'], bossResidualDamage) if currOpponentStats['Damage'] > currPlayerStats['Armor'] else str(bossResidualDamage)
				print('Boss attacks the Player for {} damage!'.format(bossAttackDamage))
			if playerKilled:
				if verbose:
					print('This kills the Player. Boss has won!')
				break

		# Switch the player for the next turn
		playersTurn = not playersTurn
		turnCount += 1
		if verbose:
			print()
	
	# Print the game outcome
	if verbose:
		print('\nGame outcome:')
		gameOutCome = 'Boss has won.' if playerKilled else 'Player has won.' if opponentKilled else 'No player has won yet.'
		gameOutCome += ' Player has spent {} Mana in total.'.format(totalManaCosts)
		print(gameOutCome)

	# Variable for the game outcome
	gameOutComeState = 0 if playerKilled else 1 if opponentKilled else 2

	# Return the outcome of the game and the total mana spent
	return gameOutComeState, totalManaCosts, castSpells


#----------------------------#
#        Main Program        #
#----------------------------#

if __name__ == "__main__":
	# Print the welcome screen
	print('''
+------------------------------------+
|                                    |
|           Advent of Code           |
|         Day 22 - Riddle 01         |
|                                    |
+------------------------------------+
	''')

	# Get the input
	with open('Day22-01_input.dat', 'r', encoding='utf-8') as content_file:
		opponentStats = {}
		for currLine in content_file.readlines():
			if 'Hit Points' in currLine:
				opponentStats['HP'] = int(currLine.strip().split(': ')[1])
			if 'Damage' in currLine:
				opponentStats['Damage'] = int(currLine.strip().split(': ')[1])
	
	# Define the spells
	spellbook = {
		'Magic Missile': {
			'cost': 53,
			'lastsTurns': 0,
			'damageOpponent': 4,
			'healingMe': 0,
			'rechargeMana': 0,
			'armorMe': 0
		},
		'Drain': {
			'cost': 73,
			'lastsTurns': 0,
			'damageOpponent': 2,
			'healingMe': 2,
			'rechargeMana': 0,
			'armorMe': 0
		},
		'Shield': {
			'cost': 113,
			'lastsTurns': 6,
			'damageOpponent': 0,
			'healingMe': 0,
			'rechargeMana': 0,
			'armorMe': 7
		},
		'Poison': {
			'cost': 173,
			'lastsTurns': 6,
			'damageOpponent': 3,
			'healingMe': 0,
			'rechargeMana': 0,
			'armorMe': 0
		},
		'Recharge': {
			'cost': 229,
			'lastsTurns': 5,
			'damageOpponent': 0,
			'healingMe': 0,
			'rechargeMana': 101,
			'armorMe': 0
		},
	}
	effectCasts = ['Shield', 'Poison', 'Recharge']
	
	# Define the player's starting stats
	playerStats = {
		'HP': 50,
		'Armor': 0,
		'Mana': 500
	}

	# Get all spell combinations, i.e. create the game tree
	totalManaSpentMinimum = float('inf')
	lowestWinningCastOrder = '-'
	# Create all combinations of spell combinations. Ignore all combinations which are "forbidden", i.e. combinations in which effect spells are cast after each other (as long as 'lastsTurns' in 'spellbook' forbids them to be cast again)
	# NB: sorting these forbidden combinations out beforehand is very important since otherwise, our game tree of depth n would grow as 5^n. With the modifications, it grows significantly less (roughly O(3^n + 2^n))
	allCastCombinations = [[f] for f in spellbook.keys()]
	currRound = 2
	while True:
		print('Creating the game tree at depth {} ...'.format(currRound))
		allCastCombinations = [f+[s] for f in allCastCombinations for s in spellbook.keys() if s=='Magic Missile' or s=='Drain' or (s=='Shield' and s not in f[-min(int(floor(spellbook['Shield']['lastsTurns']/2))-1, len(allCastCombinations)):]) or (s=='Poison' and s not in f[-min(int(floor(spellbook['Poison']['lastsTurns']/2))-1, len(allCastCombinations)):]) or (s=='Recharge' and s not in f[-min(int(floor(spellbook['Recharge']['lastsTurns']/2))-1, len(allCastCombinations)):])]
		numberOfAllGames = len(allCastCombinations)
		numberOfGamesPlayerWon = 0
		numberOfGamesUndecided = 0
		reducedCastCombinations = []
		print('Start playing at game tree depth {} ...'.format(currRound))
		for currCastOrder in allCastCombinations:
			castOrder = list(currCastOrder)
			gameOutComeState, totalManaSpent, castSpells = playGame(playerStats, opponentStats, castOrder, spellbook, hardmodeActive, False)
			if gameOutComeState==0:
				continue
			elif gameOutComeState==1:
				if totalManaSpent < totalManaSpentMinimum:
					totalManaSpentMinimum = totalManaSpent
					numberOfGamesPlayerWon += 1
					lowestWinningCastOrder = castOrder
			elif gameOutComeState==2:
				numberOfGamesUndecided += 1
				reducedCastCombinations.append(castOrder)
		allCastCombinations = reducedCastCombinations

		# Print the overall statistics:
		print('Results for round at game tree depth {}:'.format(currRound))
		print('Total number of games played: {}'.format(numberOfAllGames))
		print('Games won by the Player: {}'.format(numberOfGamesPlayerWon))
		print('Games still undecided: {}'.format(numberOfGamesUndecided))
		if numberOfGamesPlayerWon > 0:
			print('Lowest amount of Mana spent for a victory: {}'.format(totalManaSpentMinimum))
			print('Lowest-Mana winning cast order: {}'.format(lowestWinningCastOrder))
		print()
		print()

		# If all games in the current game tree lead to the death of either the Player or the Boss, the game tree is exhausted and no more games can be played
		if len(allCastCombinations) == 0:
			print('The game tree is exhausted at depth {}. No more games can be played.'.format(currRound))
			break

		# Go to the next round
		currRound += 1

	sys.exit()
