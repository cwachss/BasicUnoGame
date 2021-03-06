# Here are all the classes in one place just for my own readability purposes. Feel free to ignore, it's the same as
# what's in the other modules

import random


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

class Discard:

    def __init__(self, starting_top_card):
        self.discard_pile = [starting_top_card]
        self.top_card = starting_top_card

    def empty_discard(self):
        self.discard_pile.remove((self.top_card))
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
           print(f"{self.player_name} wins!")
        return card

    def pick_card(self, card):
        self.hand.append(card)

    def print_hand(self):
        for card in self.hand:
            if card == self.hand[-1]:
                print(card, end="")
            else:
                print(card, end=", ")

class UnoGame:

    def __init__(self, player_name):
        self.player_name = player_name
        self.deck = Deck()
        first_card = self.deck.pick_card()
        self.discard = Discard(first_card)

        player_hand = self.deck.deal_cards(cards_per_player=7)
        self.player = Player(self.player_name, player_hand)

        computer_hand = self.deck.deal_cards(cards_per_player=7)
        self.computer = Player("computer", computer_hand)

    def play_game(self):
        game_over = False
        winner = None
        turn = 1;
        while not game_over:
            if turn % 2 == 1:
                self.take_turn()
                turn += 1
            else:
                self.computer_turn()
                turn += 1

            if len(self.player.hand) == 0:
                winner = self.player.player_name
                game_over = True
            elif len(self.computer.hand) == 0:
                winner = self.computer.player_name
                game_over = True
        print(f"{winner} wins!")

    def take_turn(self):
        print(f"{self.player.player_name}'s hand: ")
        self.player.print_hand()
        print(f"\ntop card: {self.discard.top_card}")

        # add option to pick a card from the deck
        pick_or_play = input("would you like to play a card or pick one from the deck? (enter pick or play)")
        if pick_or_play == "play":

            try:
                self.input_card_to_play = input("which card would you like to play? (enter color,number)")
                self.card_details = self.input_card_to_play.split(",")
                self.card_to_play = Card(self.card_details[0], int(self.card_details[1]))

                self.player.play_card(self.card_to_play)
                self.discard.add_card(self.card_to_play)

            except (ValueError, IndexError) as e:
                print("I'm sorry, you don't have that card. Please try a different one or choose to pick a card")
                self.take_turn()
            except AssertionError:
                print("I'm sorry, that card does not match the top card. Please try a different one or choose to pick a card")
                self.take_turn()
        else:
            self.player.pick_card(self.deck.pick_card())

        print(f"{self.player.player_name}'s hand: ")
        self.player.print_hand()
        print(f"\ntop card: {self.discard.top_card}")
        print("turn over")

    def computer_turn(self):
        for i in self.computer.hand:
            if i.number == self.discard.top_card.number or i.color == self.discard.top_card.color:
                self.computer.play_card(i)
                self.discard.add_card(i)
                print(f"computer played {i}")
                print("computer turn over")
                return
        self.computer.pick_card(self.deck.pick_card())
        print("computer turn over")
