def computerDraw(drawCard(deck), rule(card), deck):
    computerCard = drawCard(deck)
    print("This card has been drawn after shuffling. The deck has",len(deck), "cards left")
    print(computerCard.value)
    print(computerCard.suit)
    computerPoints = (rule(computerCard))
    print(computerPoints, "computer's points")
    return computerPoints

