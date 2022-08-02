from Pong.game_run import Game_run


def main():
    # O numero de fps define o quão rápido a IA vai treinar
    game = Game_run(fps=500)
    game.run_game()


main()
