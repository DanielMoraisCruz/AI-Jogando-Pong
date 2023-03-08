# This code is the main file of the Pong project, here the game_run function
# is called and the game starts

from Pong.game_run import Game_run


def main():
    # The number of fps defines how fast the AI will train
    game: Game_run = Game_run(fps=200)
    game.run_game()


if __name__ == '__main__':
    main()
