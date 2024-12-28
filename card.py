from enum import Enum
from enum import IntEnum
from random import randint
from instruction import instructions
from shuffle import shuffleDeck
from rules import rule

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

#function to draw a single card from the deck of cards 
def drawCard(deck):
   randomCard = randint(0,len(deck)-1)
   drawnCard = deck.pop(randomCard)
   return drawnCard
a = drawCard
# calling the function instructions that has all the instructions to play the game. 
instructions() 
#creating dealing the entire deck of cards  
createDeck()

# User turn. Asking the user if they want to shuffle the cards 
print("It's your turn to choose a card")
choice = int(input("\nEnter 1 if you want to shuffle the deck of cards before you draw"))
#if the user wants a shuffle
if choice == 1:
  shuffleDeck(deck)
  userCard = drawCard(deck)
  #print(deck.index(userCard))
  print("This card has been drawn after shuffling. The deck has",len(deck), "cards left")
  print(userCard.value)
  print(userCard.suit)
  yourPoints = (rule(userCard))
  print(yourPoints, "your points")
#if the user doesn't want a shuffle 
else:
  print("Your card was choosen wihout reshuffle")
  userCard= drawCard(deck)
  yourPoints = (rule(userCard))
  print(userCard.value)
  print(userCard.suit)
  print("your points are:", yourPoints)

#computer's turn. asking user to give permission to computer for the turn 

x = input("Its computer's turn now. Press any key for computer's turn. Computer will shuffle everytime before choosing the card")


def computerDraw(deck):
  computerCard = drawCard(deck)
  print("This card has been drawn after shuffling. The deck has",len(deck), "cards left")
  print(computerCard.value)
  print(computerCard.suit)
  computerPoints = (rule(computerCard))
  print(computerPoints, "computer's points")
  return computerPoints


computerPoints = computerDraw(deck)

#Printing Results:

if (yourPoints> computerPoints):
   print("You win")
else:
   print("Computer Wins!")




  

