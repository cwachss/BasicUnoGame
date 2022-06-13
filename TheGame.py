from Card import Card
from Deck import Deck
from Discard import Discard
from Player import Player


class PlayGame:

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
        turn = 1
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
                input_card_to_play = input("which card would you like to play? (enter color,number)")
                card_details = self.input_card_to_play.split(",")
                card_to_play = Card(self.card_details[0], int(self.card_details[1]))

                self.player.play_card(self.card_to_play)
                self.discard.add_card(self.card_to_play)

            except (ValueError, IndexError) as e:
                print("I'm sorry, you don't have that card. Please try a different one or choose to pick a card")
                self.take_turn()
            except AssertionError:
                print("I'm sorry, that card does not match the top card. "
                      "Please try a different one or choose to pick a card")
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