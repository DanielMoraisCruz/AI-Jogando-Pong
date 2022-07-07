from Pong.run import Game_run


def main():

    game = Game_run(60)

    while game.runing:
        game.run_game()

    return 0


main()
