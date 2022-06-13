from Card import Card
import random


class Deck:
    colors = ("red", "blue", "green", "yellow")

    def __init__(self):
        self.deck = []
        for i in range(1, 10):
            for color in self.colors:
                card = Card(color, i)
                self.deck.append(card)
                self.deck.append(card)
        random.shuffle(self.deck)

    def pick_card(self):
        random_index = random.randint(1, len(self.deck)-1)
        card_picked = self.deck[random_index]
        self.deck.remove(card_picked)
        return card_picked

    def deal_cards(self, cards_per_player):
        hand = []
        for i in range(1, cards_per_player + 1):
            hand.append(self.pick_card())
        return hand

    def shuffle_discard(self, discard):
        self.deck = random.shuffle(discard)
        return self.deck