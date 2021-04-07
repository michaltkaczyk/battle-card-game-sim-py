import random
import seaborn as sns
import matplotlib.pyplot as plt


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
        self.winner = ""
        self.finished = False

    def say_state(self):
        if self.finished:
            print("Player", self.winner, "wins after", self.rounds_played, "rounds.")
        else:
            print("Game in progress,", self.rounds_played, "rounds elapsed.")
            print("Player A's hand:", self.player_a.hand)
            print("Player B's hand:", self.player_b.hand)

    def __reset_stash(self):
        self.player_a.stash = []
        self.player_b.stash = []

    def play_round(self):
        if not self.finished:
            if len(self.player_a.hand) == 0:
                self.__finish("B")
            elif len(self.player_b.hand) == 0:
                self.__finish("A")
            else:
                player_a_card = self.player_a.hand.pop(0)
                player_b_card = self.player_b.hand.pop(0)

                if player_a_card > player_b_card:
                    self.player_a.hand.extend([player_a_card, player_b_card])
                    self.player_a.hand.extend(self.player_a.stash)
                    self.player_a.hand.extend(self.player_b.stash)
                    self.__reset_stash()
                elif player_b_card > player_a_card:
                    self.player_b.hand.extend([player_b_card, player_a_card])
                    self.player_b.hand.extend(self.player_b.stash)
                    self.player_b.hand.extend(self.player_a.stash)
                    self.__reset_stash()
                else:
                    self.player_a.stash.append(player_a_card)
                    self.player_b.stash.append(player_b_card)

                self.rounds_played += 1

    def __finish(self, winner):
        self.finished = True
        self.winner = winner

    def play(self):
        while not game.finished:
            self.play_round()


if __name__ == '__main__':
    sim_rounds_elapsed = []

    for i in range(10000):
        game = Game()
        game.play()
        sim_rounds_elapsed.append(game.rounds_played)

    print(sim_rounds_elapsed)
    sns.displot(sim_rounds_elapsed, binwidth=25)
    plt.show()
