class Card:

    def __init__(self, color, number):
        self.color = color
        self.number = number

    def view_card(self):
        return self.color, self.number

    def __str__(self):
        return f"{self.color, self.number}"

    def __eq__(self, other):
        return self.color == other.color and self.number == other.number