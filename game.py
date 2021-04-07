import random


class Deck:

    def __init__(self):
        deck = list(range(13)) * 4
        random.shuffle(deck)
        self.deck = deck

    def __getitem__(self, item):
        return self.deck[item]


class Player:

    def __init__(self, hand):
        self.hand = hand
        self.stash = []


class Game:

    def __init__(self):
        self.cards = Deck()
        self.player_a = Player(self.cards[:26])
        self.player_b = Player(self.cards[26:])
        self.rounds_played = 0
        self.finished = False

    def say_state(self):
        if self.finished:
            print("Game finished after", self.rounds_played, "rounds.")
        else:
            print("Game in progress,", self.rounds_played, "rounds elapsed.")
            print("Player A's hand:", self.player_a.hand)
            print("Player B's hand:", self.player_b.hand)

    def play_round(self):
        player_a_card = self.player_a.hand.pop(0)
        player_b_card = self.player_b.hand.pop(0)

        if player_a_card > player_b_card:
            self.player_a.hand.extend([player_a_card, player_b_card])
        else:
            self.player_b.hand.extend([player_b_card, player_a_card])

        self.rounds_played += 1

    def finish(self):
        self.finished = True


if __name__ == '__main__':
    game = Game()

    game.say_state()
    game.play_round()
    game.say_state()
    game.play_round()
    game.say_state()
    game.play_round()
    game.say_state()
