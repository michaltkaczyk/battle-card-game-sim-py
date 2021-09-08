import random
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean, median
import progress

N_SIMULATIONS = 100_000


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


class Game:

    def __init__(self):
        self.cards = Deck()
        self.stash = []
        self.player_a = Player(self.cards[:26])
        self.player_b = Player(self.cards[26:])
        self.rounds_played = 0
        self.winner = ""
        self.finished = False

    def __reset_stash(self):
        self.stash = []

    def play_round(self):
        if not self.finished:
            if len(self.player_a.hand) == 0:
                self.__finish("B")
            elif len(self.player_b.hand) == 0:
                self.__finish("A")
            else:
                player_a_card = self.player_a.hand.pop(0)
                player_b_card = self.player_b.hand.pop(0)

                self.stash.extend([player_a_card, player_b_card])
                random.shuffle(self.stash)

                if player_a_card > player_b_card:
                    self.player_a.hand.extend(self.stash)
                    self.__reset_stash()
                elif player_b_card > player_a_card:
                    self.player_b.hand.extend(self.stash)
                    self.__reset_stash()
                else:
                    if len(self.player_a.hand) == 0:
                        self.__finish("B")
                    elif len(self.player_b.hand) == 0:
                        self.__finish("A")
                    else:
                        player_a_card = self.player_a.hand.pop(0)
                        player_b_card = self.player_b.hand.pop(0)

                        self.stash.extend([player_a_card, player_b_card])
                        random.shuffle(self.stash)

                self.rounds_played += 1

    def __finish(self, winner):
        self.finished = True
        self.winner = winner

    def play(self):
        while not game.finished:
            self.play_round()


if __name__ == '__main__':
    sim_rounds_elapsed = []

    for i in range(N_SIMULATIONS):
        game = Game()
        game.play()
        progress.print_progress_bar(iteration=i+1, total=N_SIMULATIONS)
        sim_rounds_elapsed.append(game.rounds_played)

    print("Mean number of rounds:", round(mean(sim_rounds_elapsed)))
    print("Median number of rounds:", round(median(sim_rounds_elapsed)))

    sns.displot(sim_rounds_elapsed, binwidth=25)
    plt.show()
