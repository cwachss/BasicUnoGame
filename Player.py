import Card


class Player:

    def __init__(self, player_name, hand):
        self.player_name = player_name
        self.hand = hand
        card_count = len(hand)

    def play_card(self, card):
        self.hand.remove(card)
        if len(self.hand) == 1:
            print("Uno!")
        elif len(self.hand) == 0:
            print(f"{self.player_name} is about to win!")
        return card

    def pick_card(self, card):
        self.hand.append(card)

    def print_hand(self):
        for card in self.hand:
            if card == self.hand[-1]:
                print(card, end="")
            else:
                print(card, end=", ")