from card import Card 

if userColor !=1 and userColor !=2:
    print ("Please enter a valid choice")
    exit()
if userColor == 1 and computerColor == "red":
    print ("You choose Red and the computer also chose Red")
if userColor == 1 and computerColor == "black": 
    print ("You choose Red and the computer chose Black \n You Win!")
if userColor == 2 and computerColor == "red":
    print ("You choose black and the computer chose Red. Computer Wins!")
if userColor == 2 and computerColor == "black": 
    print ("You choose Black and the Computer chose Black \n No one wins!")