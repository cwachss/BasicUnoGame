import Card


class Discard:

    def __init__(self, starting_top_card):
        self.discard_pile = [starting_top_card]
        self.top_card = starting_top_card

    def empty_discard(self):
        self.discard_pile.remove(self.top_card)
        temp_discard = self.discard_pile
        self.discard_pile = []
        self.discard_pile.append(self.top_card)
        return temp_discard

    def add_card(self, card_played):
        if card_played.color == self.top_card.color or card_played.number == self.top_card.number:
            self.discard_pile.append(card_played)
            self.top_card = card_played
        else:
            raise AssertionError
