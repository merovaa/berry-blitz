"""
This file contains the various essential functions required for the game to run (printBoard, move, story, challenge, playerTurn, npcTurn)
"""

# Imports nested array representing the game board
from board import board

# Required to randomize roll value and randomize trivia question
from random import randrange, choice

# Imports printing functions used for styling
from text import printSlowly, loadText

# Required to delay console text
from time import sleep

from colours import white


def printBoard(block1, block2, block3, block4, block5, block6, block7, block8,
               blockTitle, players):
  """
  Purpose: Prints text-based game board
  Parameters: Object info about each block, players
  """
  # Updates player position and their amount of Berry Bucks
  # Loops through each row
  for row in board:
    # Loops through each block in row
    for block in row:
      # Removes any players on the block
      block.players = []
  for player in players:
    # Adds the emoji of the players currently on the block to the list
    player.currentBlock.players.append(player.emoji)

  # Stores format of commonly printed strings on the board
  horizontalLine = ("-" * 94)
  spacerLine = ("|" + " " * 30 + "|" + " " * 30 + "|" + " " * 30 + "|")

  # First row
  # Prints horizontal line of dashes and empty spacer line
  print(horizontalLine)
  print(spacerLine)
  print(spacerLine)
  # Prints name of each block in first row with colouring and center alignment
  print(
      f"|{block1.colour}{block1.name:^30}{blockTitle.colour}|{block2.colour}{block2.name:^30}{blockTitle.colour}|{block3.colour}{block3.name:^30}{blockTitle.colour}|"
  )
  # Prints player emojis in the blocks, representing their position on the board
  # .join() removes the brackets and quotation marks of the list of players
  # Length of the list of players on the block is subtracted from the total width to avoid moving the borders
  print(
      f"|{''.join(block1.players):^{30 - len(block1.players)}}|{str(''.join(block2.players)):^{30 - len(block2.players)}}|{str(''.join(block3.players)):^{30 - len(block3.players)}}|"
  )
  print(spacerLine)

  # Second row
  print(horizontalLine)
  print(spacerLine)
  print(spacerLine)
  # Prints name of each block in second row with colours and center alignment
  print(
      f"|{block8.colour}{block8.name:^30}{blockTitle.colour}|{blockTitle.name:^30}|{block4.colour}{block4.name:^30}{blockTitle.colour}|"
  )
  # Prints player emojis in the blocks, representing their position on the board
  # .join() removes the brackets and quotation marks of the list of players
  # Length of the list of players on the block is subtracted from the total width to avoid moving the borders
  print(
      f"|{str(''.join(block8.players)):^{30 - len(block8.players)}}|{' '*30}|{str(''.join(block4.players)):^{30 - len(block4.players)}}|"
  )
  print(spacerLine)

  # Third row
  print(horizontalLine)
  print(spacerLine)
  print(spacerLine)
  # Prints name of each block in third row with colours and center alignment
  print(
      f"|{block7.colour}{block7.name:^30}{blockTitle.colour}|{block6.colour}{block6.name:^30}{blockTitle.colour}|{block5.colour}{block5.name:^30}{blockTitle.colour}|"
  )
  # Prints player emojis in the blocks, representing their position on the board
  # .join() removes the brackets and quotation marks of the list of players
  # Length of the list of players on the block is subtracted from the total width to avoid moving the borders
  print(
      f"|{str(''.join(block7.players)):^{30 - len(block7.players)}}|{str(''.join(block6.players)):^{30 - len(block6.players)}}|{str(''.join(block5.players)):^{30 - len(block5.players)}}|"
  )
  print(spacerLine)
  print(horizontalLine)

  print("Berry Bank: ")
  # Prints each player's amount of Berry Bucks using their emojis
  for player in players:
    print(f"{player.emoji}: {player.berryBucks}     ", end="")


def move(player):
  """
  Purpose: Rolls and moves player around the board
  Parameters: player
  """
  # Prints which player's turn it is
  printSlowly(f"\n\nIt's {player.colour}{player.name}{white}'s turn!")
  sleep(2)
  # Randomizes roll value
  roll = randrange(6)
  # Prints delayed text to simulate rolling a die
  loadText("\nRolling...")
  # Moves player one space for each number rolled
  for i in range(roll):
    # Updates player's row and column index to the next block
    player.currentBlock = board[player.currentBlock.nextRow][
        player.currentBlock.nextColumn]
  # Prints roll and landed space result to player with correct colouring
  printSlowly(
      f"\nYou rolled a {roll}! You are now at {player.currentBlock.colour}{player.currentBlock.name}{white}!"
  )


def story(player):
  """
  Purpose: Runs story when player lands on character block
  Parameter: player
  """
  ask = True
  # Prints intro and question of the appropriate story
  printSlowly("\n" + player.currentBlock.story.storyIntro)
  printSlowly("\n" + player.currentBlock.story.storyQuestion)
  # Repeats question until valid answer is given
  while ask:
    # Asks story question
    storyChoice = input("\nEnter your choice: ").lower().strip()
    if storyChoice == "a" or storyChoice == "b":
      # Breaks asking loop
      ask = False
      if storyChoice == "a":
        # If positive choice is chosen, prints corresponding outcome
        printSlowly("\n" + player.currentBlock.story.storyOutcome1)
        # Adds Berry Bucks reward
        player.berryBucks += 5
      elif storyChoice == "b":
        # If negative choice is chosen, prints corresponding outcome
        printSlowly("\n" + player.currentBlock.story.storyOutcome2)
        # Removes Berry Bucks
        player.berryBucks -= 5
    else:
      # Prompts user to give valid answer
      print("\nInvalid answer. Please try again!")


def challenge(player):
  """
  Purpose: Runs challenge when player lands on one of two of the challenge blocks
  Parameter: player
  """
  ask = True
  # Stores four different trivia questions
  triviaQuestions = "\nWhat is Strawberry Shortcake's cat's name?\nA) Pudding\nB) Taffy\nC) Custard\nD) Marmalade", "\nWhat is the name of Strawberry Shortcake's little sister?\nA) Apple Blossom\nB) Cherry Jam\nC) Apple Dumplin\nD) Ginger Snap", "\nWhich character loves singing the most?\nA) Plum Pudding\nB) Huckleberry pie\nC) Lemon Meringue\n D) Cherry Jam", "\nWhich character is a bookworm?\nA) Orange Blossom\nB) Raspberry Tart\nC) Blueberry Muffin\nD) Plum Pudding"
  # Prints challenge space instructions
  printSlowly(
      "\nYou landed on a challenge space! Here, you must answer a Strawberry Shortcake trivia question correctly in order to receive Berry Bucks. Be careful as a wrong answer results in losing Berry Bucks!"
  )
  # Prints random trivia question from list
  printSlowly(choice(triviaQuestions))
  # Repeats question until valid answer is given
  while ask:
    # Stores player's answer to question
    triviaAnswer = input("\nEnter your answer: ").lower().strip()
    # Checks if answer is valid
    if triviaAnswer == "a" or triviaAnswer == "b" or triviaAnswer == "c" or triviaAnswer == "d":
      ask = False
      # If answer is correct, prints message and adds Berry Bucks
      if triviaAnswer == "c":
        ask = False
        print("\nThat is correct, amazing job! You won 5 Berry Bucks.")
        player.berryBucks += 5
      # If answer is incorrect, prints message and removes Berry Bucks
      else:
        print("\nOh no, that is incorrect! You lost 5 Berry Bucks.")
        player.berryBucks -= 5
    else:
      # Prompts user to give valid answer
      print("Invalid answer. Please try again!")


def playerTurn(player):
  """
  Purpose: Handles player turns
  Parameter: player
  """
  # Rolls and moves player
  move(player)
  # Checks if player landed on challenge space
  if player.currentBlock == board[0][2] or player.currentBlock == board[2][0]:
    challenge(player)
  # Checks if player landched on their own character's block
  elif player.currentBlock == player.homeBlock:
    ask = True
    # Repeats question until valid answer is given
    print(
        "\nYou've landed on your home block! Do you quickly run inside to grab some Berry Bucks?\nA) Yes, let's go!\nB) No, let's just continue the journey.\n"
    )
    while ask:
      # Asks player for action choice
      homeBlockChoice = input("\nEnter your choice: ").lower().strip()
      # Checks if answer is valid
      if homeBlockChoice == "a" or homeBlockChoice == "b":
        # Ends loop when valid answer is given
        ask = False
        # Adds Berry Bucks
        if homeBlockChoice == "a":
          player.berryBucks += 10
          print(
              "\nGood choice! You grabbed 10 Berry Bucks. Let's continue our journey, roll again!"
          )
        if homeBlockChoice == "b":
          print("\nOkay, let's keep going. Roll again!")
        # Player rolls again
        playerTurn(player)
    else:
      # Prompts user to give valid answer
      print("\nInvalid answer. Try again!")
  else:
    # Prints story if player lands anywhere else (which is always a character block)
    story(player)
    input("\nEnter a key to continue: ")


def npcTurn(player):
  """
  Purpose: Handles NPC turns in singleplayer mode, does not display story to player
  Parameter: player
  """
  # Prints which player's turn it is
  printSlowly(f"\n\nIt's {player.colour}{player.name}{white}'s turn!")
  # Randomizes roll value
  roll = randrange(6)
  for i in range(roll):
    # Updates player's (excluding played character) current block
    # Updates player's row and column index to the next block
    player.currentBlock = board[player.currentBlock.nextRow][
        player.currentBlock.nextColumn]
  # Prints delayed text to simulate rolling a die
  loadText(f"\n{player.colour}{player.name}{white} is rolling...")
  # Prints NPC's turn result to player
  printSlowly(
      f"\n{player.colour}{player.name}{white} rolled a {roll}. She is now at {player.currentBlock.name}!"
  )
  # Randomizes whether the NPC gains or loses Berry Bucks and updates amount
  gainLose = randrange(2)
  if gainLose == 1:
    player.berryBucks += 5
    printSlowly(f"\n{player.colour}{player.name}{white} gained 5 Berry Bucks.")
  else:
    player.berryBucks -= 5
    printSlowly(f"\n{player.colour}{player.name}{white} lost 5 Berry Bucks.")
