def rule(drawnCard):
    points = 0

    if drawnCard.suit == "spade":
        points = points+4
    if drawnCard.suit == "heart":
        points = points +3
    if drawnCard.suit == "diamond":
        points = points+2
    if drawnCard == "club":
        points = points +1

    totalPoints = points +drawnCard.value
    return totalPoints


