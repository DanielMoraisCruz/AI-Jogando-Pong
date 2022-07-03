from Pong.run import Game_run


def main():
    """Funcao de inicializacao

    Quando o bot inicia:
        1 - Abre Pong
        2 - Comecar a Rede Neural
    Returns:
        _type_: _description_
    """

    game = Game_run(60)

    while game.runing:
        game.curr_menu.display_menu()
        game.game_loop()

    return 0


main()
