import random

class DosCardGame:
    def __init__(self, num_players=2):
        self.num_players = num_players
        self.players = [Player() for _ in range(num_players)]
        self.deck = self.initialize_deck()
        self.current_player = 0
        self.current_number = None
        self.current_color = None
        self.played_cards = []

    def initialize_deck(self):
        colors = ['Red', 'Blue', 'Green', 'Yellow']
        numbers = list([1, 3, 4, 5]) * 3 + list([6, 7, 8, 9, 10]) * 2
        deck = [(color, number) for color in colors for number in numbers]
        random.shuffle(deck)
        return deck

    def deal_initial_cards(self):
        for _ in range(7):
            for player in self.players:
                player.add_card(self.deck.pop())

    def play_card(self, player_index, card_index):
        card = self.players[player_index].play_card(card_index)
        if self.is_valid_move(card):
            self.played_cards.append(card)
            self.current_number = card[1]
            self.current_color = card[0]
        else:
            print("Invalid move. Try again.")

    def is_valid_move(self, card):
        return card[0] == self.current_color or card[1] == self.current_number

    def next_turn(self):
        self.current_player = (self.current_player + 1) % self.num_players

    def display_game_state(self):
        print(f"\nCurrent Player: {self.current_player + 1}")
        print(f"Current Card: {self.current_color} {self.current_number}")
        print("Played Cards:", self.played_cards)
        for i, player in enumerate(self.players):
            print(f"Player {i + 1} Hand: {player.hand}")

    def play(self):
        print("Starting Dos Card Game!")
        self.deal_initial_cards()

        while not any(player.is_winner() for player in self.players):
            self.display_game_state()

            player_input = input("Player, enter 'play' to play a card: ")
            if player_input.lower() == 'play':
                card_index = int(input("Enter the index of the card to play: ")) - 1
                self.play_card(self.current_player, card_index)
                self.next_turn()

        winning_player = [i + 1 for i, player in enumerate(self.players) if player.is_winner()][0]
        print(f"\nPlayer {winning_player} wins!")

class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def play_card(self, index):
        return self.hand.pop(index)

    def is_winner(self):
        return not self.hand

if __name__ == "__main__":
    dos_game = DosCardGame(num_players=2)
    dos_game.play()
