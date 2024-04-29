"""
This file contains the functions and variables that are required to customize the game (setGameMode, setCharacters, setGameDuration)
"""

# Necessary to choose random characters for NPCs
from random import choice

# Imports printing functions used for styling
from text import printSlowly, loadText

# Necessary for clearing the console
import os

# Imports colour codes for board styling
from colours import blue, magenta, orange, pink, purple, yellow, white

# Stores players
players = []


def setGameMode():
  """
  Purpose: Sets game to either multiplayer or singleplayer mode
  Return: gameMode
  """
  # Prompts the user to select the game mode
  printSlowly(
      "Select your game mode:\nA) Multiplayer (PvP)\nB) Singleplayer (PvC)")
  ask = True
  # Repeats question until valid answer is given
  while ask:
    gameMode = input("\nEnter your choice: ").lower().strip()
    # Checks if valid answer is given
    if gameMode == "a" or gameMode == "b":
      # Ends loop when valid answer is given
      ask = False
    else:
      # Prompts user to provide valid answer
      print("Invalid input. Please try again! ")
  os.system("clear")
  # Returns whether game is in multiplayer or singleplayer mode
  return gameMode


def setCharacters(gameMode, characters):
  """
  Purpose: Determines the character choice of each player
  Parameters: gameMode, characters
  Return: numPlayers
  """
  ask = True
  # Repeats question until valid answer is given
  while ask:
    # Asks user how many players there are
    numPlayers = int(input("Enter the number of players (2-6): "))
    # Checks if answer is within 2-6 player range
    if numPlayers >= 2 and numPlayers <= 6:
      # Ends loop when valid answer is given
      ask = False
    else:
      # Prompts user to enter valid answer
      printSlowly(
          "Invalid input. Please ensure your choice is within the possible range of players. "
      )

  def chooseCharacters(numPlayers):
    """
    Purpose: Handles character choices within the setCharacters function
    Parameter: numPlayers
    """
    # Multiplayer mode
    if gameMode == "a":
      os.system("clear")
      # Locally stores chosen characters
      chosenCharacters = []
      # Loops for each player
      for i in range(numPlayers):
        os.system("clear")
        ask = True
        # Repeats question until valid answer is given
        while ask:
          # Asks for character choice of player
          printSlowly(f"Which character would player {i + 1} like to play as?")
          # Prints choices
          print(
              f"A) {pink}Strawberry Shortcake{white}\nB) {orange}Orange Blossom{white}\nC) {purple}Plum Pudding{white}\nD) {yellow}Lemon Meringue{white}\nE) {magenta}Raspberry Tart{white}\nF) {blue}Blueberry Pie{white}\n\n"
          )
          # Stores character choice
          characterChoice = input("Enter your choice: ").lower().strip()
          # Checks if choice corresponds to options
          if characterChoice == "a" or characterChoice == "b" or characterChoice == "c" or characterChoice == "d" or characterChoice == "e" or characterChoice == "f":
            # Checks if character has already been chosen
            if characterChoice not in chosenCharacters:
              # Breaks loop if answer is valid
              ask = False
              # Adds choice to list of chosen characters
              chosenCharacters.append(characterChoice)
              # Loops through each available character choice
              for character in characters:
                # Checks if character is chosen
                if characterChoice == character.letter:
                  # Adds character to list of players
                  players.append(character)
            else:
              # Prompts user to provide valid response
              print("\nInvalid answer. Please try again!")

    # Singleplayer mode
    if gameMode == "b":
      os.system("clear")
      # Locally stores chosen characters
      chosenCharacters = []
      ask = True
      # Repeats question until answer is valid
      while ask:
        # Prints character options
        printSlowly(f"Which character would you like to play as?")
        print(
            f"A) {pink}Strawberry Shortcake{white}\nB) {orange}Orange Blossom{white}\nC) {purple}Plum Pudding{white}\nD) {yellow}Lemon Meringue{white}\nE) {magenta}Raspberry Tart{white}\nF) {blue}Blueberry Pie{white}\n"
        )
        # Stores character choice for player 1
        characterChoice = input("Enter your choice: ").lower().strip()
        # Checks if choice corresponds to options
        if characterChoice == "a" or characterChoice == "b" or characterChoice == "c" or characterChoice == "d" or characterChoice == "e" or characterChoice == "f":
          ask = False
          # Adds choice to list of chosen characters
          chosenCharacters.append(characterChoice)
        else:
          # Prompts user to provide valid response
          print("\nInvalid answer. Please try again!")

      # Loops until a character has been chosen for each player
      while len(chosenCharacters) < numPlayers:
        # Picks random character for player
        randomCharacter = choice(["a", "b", "c", "d", "e", "f"])
        # Checks if random character has not already been chosen
        if randomCharacter not in chosenCharacters:
          # Adds random character to list of chosen characters
          chosenCharacters.append(randomCharacter)
      # Loops through each available character choice
      for character in characters:
        # Loops through each chosen character
        for chosenCharacter in chosenCharacters:
          # Checks if character is chosen
          if chosenCharacter == character.letter:
            # Adds character to list of players
            players.append(character)

  # Multiplayer mode
  if gameMode == "a":
    os.system("clear")
    printSlowly(
        "You have chosen multiplayer mode. Let's get you and your friends set up..."
    )
    # Asks each player which character they choose and adds to list of players
    chooseCharacters(numPlayers)

  # Singleplayer Mode
  elif gameMode == "b":
    os.system("clear")
    printSlowly("You have chosen singleplayer mode. Let's set up the game...")

    # Asks main player which character they choose and randomizes characters for NPCs
    chooseCharacters(numPlayers)

    # Prints to user to simulate loading the characters
    loadText("Generating opponent(s)...")

    # Prints player list to user
    print("\nHere are the players:\n")
    for player in players:
      print(f"{player.colour}{player.name}\033[97m")
    input("\nEnter a key to continue: ")
    os.system("clear")
  return numPlayers


def setGameDuration():
  """
  Purpose: Sets how long the game goes (based on how many times each player rolls)
  Return: numRolls
  """
  ask = True
  os.system("clear")
  # Prints duration choices
  printSlowly(
      "How long should our journey last?\nA) Just the morning (2 rolls each)\nB) Half the day (3 rolls each)\nC) Whole day (6 rolls each)\n"
  )
  # Repeats question until valid answer is given
  while ask:
    # Stores user's duration choice
    durationChoice = input("Enter your choice: ")
    # Checks if choice is valid
    if durationChoice == "a" or durationChoice == "b" or durationChoice == "c" or durationChoice == "d":
      # Breaks loop if answer is valid
      ask = False
    else:
      # Prompts user to provide valid answer
      print("Invalid answer. Please try again!")
  # Sets initial number of rolls (turns) to zero
  numRolls = 0
  # Checks duration choice and sets numRolls to corresponding number
  if durationChoice == "a":
    numRolls = 2
    return numRolls
  elif durationChoice == "b":
    numRolls = 3
    return numRolls
  elif durationChoice == "c":
    numRolls = 6
  return numRolls
