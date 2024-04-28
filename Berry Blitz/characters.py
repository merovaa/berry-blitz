"""
This file contains the object information for the six different characters of the game.
"""

# Imports nested array representing the game board
from board import board

# Imports colour codes for board styling
from colours import blue, magenta, orange, pink, purple, yellow


class Character:
  """
  Purpose: Initializes a Character object
  Parameters: Name of the character, character's colour theme, character's emoji representation on the board, corresponding letter option during set up, character's current block, their home block, and their amount of Berry Bucks)
  """

  def __init__(self, characterName, characterColour, characterEmoji,
               characterLetter, currentBlock, homeBlock, berryBucks):
    self.name = characterName
    self.colour = characterColour
    self.emoji = characterEmoji
    self.letter = characterLetter
    self.currentBlock = currentBlock
    self.homeBlock = homeBlock
    self.berryBucks = berryBucks


# Sets current block of all players to the top-left (Strawberry's House)
currentBlock = board[0][0]

# Stores attributes of each character
# In the homeBlock attribute, first index represents the row while the second index represents the column
strawberry = Character("Strawberry Shortcake", pink, "🍓 ", "a", currentBlock,
                       board[0][0], 15)
orange = Character("Orange Blossom", orange, "🍊 ", "b", currentBlock,
                   board[0][1], 15)
plum = Character("Plum Pudding", purple, "💜 ", "c", currentBlock, board[1][2],
                 15)
lemon = Character("Lemon Meringue", yellow, "🍋 ", "d", currentBlock,
                  board[2][2], 15)
raspberry = Character("Raspberry Tart", magenta, "🩷 ", "e", currentBlock,
                      board[2][1], 15)
blueberry = Character("Blueberry Pie", blue, "🫐 ", "f", currentBlock,
                      board[0][1], 15)

# Stores all of the available characters in the game
characters = [strawberry, orange, plum, lemon, raspberry, blueberry]
