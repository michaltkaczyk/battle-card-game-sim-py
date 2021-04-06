class Game:

    def __init__(self, finished=False, rounds_played=0):
        self.finished = finished
        self.rounds_played = rounds_played

    def say_state(self):
        if self.finished:
            print("Game finished after", self.rounds_played, "rounds")
        else:
            print("Game in progress after", self.rounds_played, "rounds")

    def play_new_round(self):
        self.rounds_played += 1

    def finish(self):
        self.finished = True


if __name__ == '__main__':
    game = Game()

    game.say_state()
    game.play_new_round()
    game.say_state()
    game.finish()
    game.say_state()
