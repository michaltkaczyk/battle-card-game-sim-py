import random


class Deck:

    def __init__(self):
        deck = list(range(13)) * 4
        random.shuffle(deck)
        self.deck = deck

    def __getitem__(self, item):
        return self.deck[item]


class Game:

    def __init__(self, finished=False, rounds_played=0):
        self.finished = finished
        self.rounds_played = rounds_played

    def say_state(self):
        if self.finished:
            print("Game finished after", self.rounds_played, "rounds.")
        else:
            print("Game in progress,", self.rounds_played, "rounds elapsed.")

    def play_round(self):
        self.rounds_played += 1

    def finish(self):
        self.finished = True


class Player:

    def __init__(self, hand, stash=None):
        self.hand = hand
        if stash is None:
            self.stash = []


if __name__ == '__main__':
    cards = Deck()

    player_a = Player(cards[:26])
    player_b = Player(cards[26:])

    print(player_a.hand)
    player_a.hand.pop(0)
    print(player_a.hand)

    game = Game()
    game.say_state()
    game.play_round()
    game.say_state()
    game.finish()
    game.say_state()



