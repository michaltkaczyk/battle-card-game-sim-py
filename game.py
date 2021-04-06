class Game:

    def __init__(self, finished):
        self.finished = finished

    def say_state(self):
        if self.finished:
            print("Game finished!")
        else:
            print("Game in progress...")


if __name__ == '__main__':
    game = Game(finished=True)

    game.say_state()
