from Card import Card
import random


class Deck:
    colors = ("red", "blue", "green", "yellow")

    def __init__(self):
        self.deck = []
        for i in range(0, 3):
            for color in self.colors:
                card = Card(color, i)
                self.deck.append(card)
                # self.deck.append(card)
        random.shuffle(self.deck)
        self.empty = False

    def pick_card(self):
        # length_of_deck = len(self.deck)-1
        # random_index = random.randint(1, length_of_deck)
        card_picked = self.deck.pop()
        # self.deck.remove(card_picked)
        if len(self.deck) == 0:
            self.empty = True
        return card_picked

    def deal_cards(self, cards_per_player):
        hand = []
        for i in range(1, cards_per_player + 1):
            hand.append(self.pick_card())
        return hand

    def shuffle_discard(self, discard):
        self.deck = discard
        return self.deck
