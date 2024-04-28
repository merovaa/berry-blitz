"""
This file contains the object information for the text-based game board.
"""

# Imports colour codes for board styling
from colours import blue, green, magenta, orange, pink, purple, white, yellow

# Imports story object information
from stories import *


class Board:
  """
  Purpose: Initializes a Board object
  Parameters: Name of the block, colour of the block's text, row index of the next block, column index of the next block, list of players currently on the block, corresponding story (except on title block)
  """

  def __init__(self, blockName, blockColour, nextRow, nextColumn, blockPlayers,
               blockStory):
    self.name = blockName
    self.colour = blockColour
    self.nextRow = nextRow
    self.nextColumn = nextColumn
    self.players = blockPlayers
    self.story = blockStory


# Stores attributes of each block
# blockPlayers has six empty spaces for the emojis which are later added when moving around the board
# Story is set to None for blockTitle as it is not a block that players will land on
block1 = Board("Strawberry's House", pink, 0, 1, [], story1)
block2 = Board("Orange's Boutique", orange, 0, 2, [], story2)
block3 = Board("Challenge", green, 1, 2, [], 0)
block4 = Board("Plum's Cinema", purple, 2, 2, [], story4)
block5 = Board("Lemon's Garden", yellow, 2, 1, [], story5)
block6 = Board("Raspberry's Bakery", magenta, 2, 0, [], story6)
block7 = Board("Challenge", green, 1, 0, [], 0)
block8 = Board("Blueberry's Library", blue, 0, 0, [], story8)
blockTitle = Board("BERRY BLITZ", white, 0, 0, [], None)

# Represents the board
# Nested lists represent rows
board = [[block1, block2, block3], [block8, blockTitle, block4],
         [block7, block6, block5]]
