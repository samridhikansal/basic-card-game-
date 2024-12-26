from enum import Enum
from enum import IntEnum

class Card:
  def __init__(self, suit, value):
    self.suit= suit
    self.value= value

class Suit(Enum):
  SPADE = "spade"
  DIAMOND = "diamond"
  HEART = "heart"
  CLUB = "club"

class Value(IntEnum):
  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  SIX = 6
  SEVEN = 7
  EIGHT = 8
  NINE = 9
  TEN = 10
  JACK = 11
  QUEEN = 12
  KING = 13
  ACE = 14

deck = []

for suit in Suit:
  for value in Value:
    deck.append(Card(Suit(suit), Value(value)))

print(len(deck))
  

  
# This class defines a simple class of cards. Each card has a color, a number and a type. 