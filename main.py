"""This code is the main file of the Pong project, here the game_run function
is called and the game starts"""

from Pong.game_run import Game_run  # Import the game_run class

# The number of fps defines how fast the AI will train
FPS = 400


def main():
    # The number of fps defines how fast the AI will train
    game: Game_run = Game_run(fps=FPS)  # Create the game object
    game.run_game()  # Start the game


if __name__ == '__main__':  # If the file is run directly
    main()  # Run the main function
