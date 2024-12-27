from enum import Enum
from enum import IntEnum
from random import randint

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

#Empty deck of cards 
deck = []

#function to deal the full deck of cards 
def createDeck():
    for suit in Suit:
        for value in Value:
            deck.append(Card(Suit(suit), Value(value)))
    return deck

#function to draw a sinle card from the deck of cards 
def drawCard(deck):
   randomCard = randint(0, len(deck)-1)
   print(deck.pop(randomCard).suit)
   print(deck.pop(randomCard)).value
   return deck.pop(randomCard)
   
createDeck()
drawCard(deck)


  

  
# This class defines a simple class of cards. Each card has a color, a number and a type. 