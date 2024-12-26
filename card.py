from enum import Enum

class Card:
  
  def __init__(self, suit, value):
    self.suit= suit
    self.value= value

class cardDeck(Enum):
  SPADE = "spade"
  DIAMOND = "diamond"
  HEART = "heart"
  CLUB = "club"

  print(SPADE)
  
# This class defines a simple class of cards. Each card has a color, a number and a type. 