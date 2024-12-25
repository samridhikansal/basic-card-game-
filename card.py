class Card:
  def __init__(self, color, name, type):
    self.color = color
    self.name = name
    self.type = type

p1 = Card("Red", 10, "diamond")

print(p1.name)
print(p1.color)
print(p1.type)