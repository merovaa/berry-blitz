"""
This file contains the story-based text of the game as well as functions that control the printing style.
"""

# Necessary for clearing and delaying the console text
from time import sleep


def printSlowly(text):
  """
  Purpose: prints text letter by letter, creating a more realistic user experience
  Parameter: text
  Mostly taken from online resource, slightly modified to fit program
  https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
  """
  for char in text:
    print(char, end="", flush=True)
    sleep(0.05)
  print()


def loadText(text):
  """
  Purpose: delays trailing ellipses of text, creating a loading screen experience
  Parameter: text
  """
  dots = text[-3:]
  print(text[:-3], end="")
  for letter in dots:
    print(letter, end='', flush=True)
    sleep(1)
  print()


# Printed when game is launched
introText = "Welcome to Berry Blitz! 🍰\nThis captivating game takes Strawberry Shortcake and her best friends on thrilling adventures while trying to collect as many Berry Bucks as possible.\nBe prepared to discover new areas of Strawberry Land, make new friends, and also make important decisions that’ll help you explore a berrylicious trip like no other!\nSo without further a due, grab your Berry Bucks and let's begin your sweetest adventure yet!"

# Printed after introductory text
instructions = "\n\nWelcome to the game board!\nIn this game, you'll each begin with 15 Berry Bucks with the objective of finishing with the most in the end.\nTaking turns, you'll each roll and travel around the board. Depending on where you land, you'll go through a mini scenario where your choices will influence whether you gain or lose Berry Bucks.\nIn the challenge squares, you'll also have the chance to gain or lose some bucks.\nFinally, the player who finishes with the most Berry Bucks wins!"
"""
The following variables contain the text for each story in the game. The strings contain the introductory text, question prompt, and two outcome texts, respectively.
"""
story1Text = (
    "You spot a quaint home in the distance with a red exterior and green leafy roof with daisies surrounding it. You stroll up to it and knock on the tall wooden door. There’s a small message on the door that reads “Not home right now! Check under the flower pot next to the door”. You lift the clay flower pot to reveal a golden strawberry-shaped key. You proceed to unlock the front door and enter. In front of you, Strawberry Shortcake’s cat, Custard, looks at you with big green eyes. She seems hungry! Should you feed Custard? Hold on… you begin to smell a sweet and citrusy aroma coming from the kitchen. As you approach the oven, you see that two big strawberry pies are baking and there’s a timer with just a minute left!",
    "What do you do?\nA) Feed Custard some pie with milk\nB) Take the pies out and leave them to cool",
    "Oh no! Custard is allergic to milk. You lost 5 Berry Bucks.",
    "Phew! Turns out Custard's actually allergic to milk. Strawberry Shortcake is glad you were there to take out the pies! You earned 5 Berry Bucks."
)

story2Text = (
    "You finally make your way to Orange Blossom’s Boutique, how exciting! You suddenly stumble upon a beautiful pink dress that has your name written all over it in the window of the store. You decide to check it out, but as soon as you walk into the store, you realize that there’s a huge sale going on and the staff desperately needs help with managing the store.",
    "What do you do?\nA) Help the staff\nB) Buy the dress",
    "The staff appreciates your help and gifts you with 5 Berry Bucks. Nice one!",
    "The staff are so busy that they accidentally overcharge you for the dress. You lost 5 Berry Bucks."
)

story4Text = (
    "You feel the need to take a break from your mystical journey, so you decide to stop by Plum Pudding’s Cinema to watch the coolest movie out right now, “Baking in Berrytown”. You grab your ticket and go to pick out your favourite snacks, but as soon as you leave the concession stand, you notice that the popcorn machine is broken. Popcorn is flying everywhere and the fizzy fruit juice machine is spilling your favorite Blueberry soda on the ground! Unfortunately, when you call out to see if anyone is there you hear muffled voices coming from behind. You start to notice a big commotion going on, everyone is panicking!",
    "What do you do?\nA) Help the staff and fix the machines, but miss the start of the movie\nB) Escape the commotion and enter the cinema",
    "You stay calm and assist the staff. Eventually, the machines stop malfunctioning and all is good! The workers give you 5 Berry Bucks to make up for the part of the movie you missed.",
    "You're so excited to see the movie that you run into the theater. A few minutes later, it's announced that the movie is cancelled due to the Blueberry Soda causing a flood! Oh no! You lost 5 Berry Bucks."
)

story5Text = (
    "Finally, you get a breath of fresh air from Lemon Meringue's magical garden, filled with lemons and strawberries almost the size of your head. You hear birds chirping your favorite melody and see a huge statue of Lemon Meringue in the middle of the garden. You smell the fresh cherry blossoms blooming in the springtime and see beautiful pink and yellow roses. You then head to a wooden swing that’s being held up by the most beautiful vines covered with bright sunflowers. As you’re swinging, you start to notice a noise in the flower-covered pink shed behind you. You decide to get up and check out if anyone is there. Fortunately, you see Lemon Meringue’s dog, Frappe, with a note attached to his collar. The note says, 'To whoever found this, it’s the perfect time to make my Lemon Meringue pie. Unfortunately, I can’t pick the lemons myself, since I’m away on a journey. Would you be a dear and pick 10 for me? They’re by the blueberries. Thank You! P.S. Since you helped me, there’s a baker's dozen lemon donuts near the window.' You want to help your friend, but you don’t have enough time and you’re starting to get really hungry.",
    "What do you do?\nA) Stay and pick the lemons\nB) Grab the donuts and leave",
    "You pick the ten lemons, and although tired and hungry, feel proud that you helped your friend out. You enjoy the donuts in the sunny meadow and are awarded 5 Berry Bucks.",
    "You eat the donuts and are no longer hungry. However, you now feel the need to pay for eating the donuts without helping, so you lose 5 Berry Bucks."
)

story6Text = (
    "As you're making your way through town, the delicious smell of cake surrounds you. You decide to follow the scent, and eventually end up at a magenta-coloured sign that reads 'Raspberry Tart’s Bakery'. You swing the door open and a chime of bells signify your arrival. You call out 'Is anyone there?' but receive no response. You decide to look around and find a note taped on the refrigerator. It says 'I had to run out to grab some flour. If anyone is reading this, please check on my cakes in the oven! - Raspberry'. Unfortunately, you were responsible for bringing a birthday cake to the party you were attending later today. The next closest bakery is an hour away, but the party starts in half an hour!",
    "What do you do?\nA) Stay to look after the cakes\nB) Leave and go to the next bakery",
    "You decide to stay and look after the cakes. While waiting, you find ingredients which you use to make the birthday cake you needed by yourself. You eventually make it to the birthday party and earn 5 Berry Bucks!",
    "You were late to the party and when you arrive, you realize that the cakes in the oven that burned were also for the party! You lost 5 Berry Bucks."
)

story8Text = (
    "You come across a huge dark blue book-shaped structure that happens to have a door in the front of it. Woah! It’s a bookstore, how cute! As you enter the bookstore, which has a hot chocolate bar and the coziest vibe in town, you begin to stroll through each row of shelves, seeing the various options. Suddenly, you come across a note that reads, 'Hey there! It’s Blueberry, I had to head out for a second to grab a Shaken Blueberry Espresso. Take care of the store for me please, thanks!' You’re shocked… this is such a big responsibility! As soon as you try to head out, a crowd of people start rushing in, and start rummaging through the shelves and making a ruckus.",
    "What do you do?\nA) Take over the cash register and assist customers trying to buy books\nB) Take over the hot chocolate bar and start serving customers",
    "Good choice! Slowly, the rush slows down and all is back to normal. You earned 5 Berry Bucks for your help!",
    "Oh no! Turns out there was no one at the cash register so the customers assumed the books were for free and left. You lost 5 Berry Bucks."
)
