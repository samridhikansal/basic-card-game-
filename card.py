class Card:
  
  type = ["diamond", "heart", "spade", "club"]
  color = ["red", "black"]
  number = range(1,14)
  def __init__(self, color, number, type):
    self.color = color
    self.number = number
    self.type = type
  def __str__(self):
    cardType = str(self.type)
    cardColor = str(self.color)
    cardNumber = str(self.number)
    result = cardType + " " + cardColor + " " + cardNumber
    return(result)
  
  
# This class defines a simple class of cards. Each card has a color, a number and a type. 