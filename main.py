"""
ICS 3UI Text Based Game Project
"Berry Blitz" by Meryam Akhundova
April 27th, 2024

This program is a text-based board game based on the Strawberry Shortcake series. 

This file contains the basic components of the game and is responsible for managing the general flow.
"""

# Imports essential functions for the game
from utilities import printBoard, playerTurn, npcTurn

# Imports required text and printing functions
from text import introText, instructions, printSlowly, loadText

# Imports object attributes for each board space
from board import block1, block2, block3, block4, block5, block6, block7, block8, blockTitle

# Imports game configuration information
from setup import setGameMode, setCharacters, setGameDuration, players

# Imports list of available characters
from characters import characters

# Required to clear console
import os

# Initializes the number of players
numPlayers = 0


def multiplayerMode(numRolls, players):
  """
  Purpose: Runs game in multiplayer mode
  Parameters: numRolls, players
  """
  # Loops through for the number of rounds
  for i in range(numRolls):
    # Prints board and runs turn for each player
    for player in players:
      os.system("clear")
      printBoard(block1, block2, block3, block4, block5, block6, block7,
                 block8, blockTitle, players)
      playerTurn(player)


def singleplayerMode(numRolls, players, numPlayers):
  """
  Purpose: Runs game in singleplayer mode
  Parameter: numRolls, players, numPlayers
  """
  # Loops for the number of rounds
  for i in range(numRolls):
    os.system("clear")
    printBoard(block1, block2, block3, block4, block5, block6, block7, block8,
               blockTitle, players)
    # Runs turn for main player
    playerTurn(players[0])
    # Loops for remaining players
    for i in range(1, numPlayers):
      os.system("clear")
      printBoard(block1, block2, block3, block4, block5, block6, block7,
                 block8, blockTitle, players)
      # Runs condensed NPC turn for each player
      npcTurn(players[i])
      input("\nEnter a key to continue: ")


def endGame():
  """
  Purpose: Reveals winner when the game is over
  """
  # Prints to user that game has ended
  printSlowly("\nWe've reached the end of our journey!")
  loadText("\nLet's see who our winner is...")

  # Loops through players and dinds the highest number of Berry Bucks
  maxBerryBucks = max(player.berryBucks for player in players)

  # Stores winner(s)
  winners = []

  # Loops through players
  for player in players:
    if player.berryBucks == maxBerryBucks:
      # Adds player to list of winners if they have the max Berry Bucks amount
      winners.append(player.name)

  # Prints singular winner message when there is one winner
  if len(winners) == 1:
    print(
        f"\nCongratulations, {''.join(winners)}! You finished with the most Berry Bucks. Way to go!"
    )
  # Prints plural winner message when there are multiple winners
  else:
    print(
        f"\nCongratulations, {' and '.join(winners)}! You tied for finishing with the most Berry Bucks. Way to go!"
    )
    print("Hope you found this game berry fun! See you next time 🍰")


def main():
  """
  Purpose: Manages the flow of the entire game
  """
  # Introduction to game
  printSlowly(introText)
  input("\nEnter a key to continue: ")
  printBoard(block1, block2, block3, block4, block5, block6, block7, block8,
             blockTitle, players)
  printSlowly(instructions)
  input("\nEnter a key to continue: ")
  os.system("clear")
  # Setting up the game
  gameMode = setGameMode()
  numPlayers = setCharacters(gameMode, characters)
  numRolls = setGameDuration()
  # Gameplay
  if gameMode == "a":
    multiplayerMode(numRolls, players)
  if gameMode == "b":
    singleplayerMode(numRolls, players, numPlayers)
  endGame()


main()
