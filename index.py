import random
from card import deck


print ("Welcome to the card game!")
print("\n You will be playing against the computer")
print ("\n The one who picks the best card wins the game")
print("\n You will pick the card first and then the computer will pick the card")
print( "\n All the best !! Have fun!!")
userColor = int(input("\n Enter 1 for Red and 2 for Black: "))
userType = int(input("spade or club or diamond or heart"))
userNumber = int( input("Enter the number of your card:"))
print( userColor)
print (userType)
print (userNumber)

computerColor = random.choice(cardColor)
computerType = random.choice(cardType)
computerNumber = random.randint(1,14)
print(computerType)
print(computerColor)
print(computerNumber)

computerFinal = Card(computerColor, computerNumber,computerType)
userFinal = Card(userColor, userNumber, userType)


