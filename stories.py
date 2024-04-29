"""
This file contains the object information for the different stories in the game that appear when a player lands on a character block.
"""

# Imports arrays of text for each story
from text import story1Text, story2Text, story4Text, story5Text, story6Text, story8Text


class Story:
  """
  Purpose: Initializes a Story object
  Parameters: Introductory text of the story, question prompt text, outcome of the first choice, outcome of the second choice
  """

  def __init__(self, storyIntro, storyQuestion, storyOutcome1, storyOutcome2):
    self.storyIntro = storyIntro
    self.storyQuestion = storyQuestion
    self.storyOutcome1 = storyOutcome1
    self.storyOutcome2 = storyOutcome2


# Stores different components of the story from the imported arrays of text
story1 = Story(story1Text[0], story1Text[1], story1Text[2], story1Text[3])
story2 = Story(story2Text[0], story2Text[1], story2Text[2], story2Text[3])
story4 = Story(story4Text[0], story4Text[1], story4Text[2], story4Text[3])
story5 = Story(story5Text[0], story5Text[1], story5Text[2], story5Text[3])
story6 = Story(story6Text[0], story6Text[1], story6Text[2], story6Text[3])
story8 = Story(story8Text[0], story8Text[1], story8Text[2], story8Text[3])
