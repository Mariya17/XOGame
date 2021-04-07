import XOBoard


def playXOGame():
    """
    main function
    Start:
        1. Print an empty board
        2. Loop - give to users fill the board with X/O
            2.0. Check if the move is valid
            2.1. Check score status
            2.2. Print the board
            2.3. Finish the game in case of win od draw

    :return:
    """
    game_board = XOBoard.XOBoard()
    game_board.Display()

    for i in range(game_board.sizeOfBoard):
        character = game_board.gameCharacters[i % 2]
        game_board.Put(character)
        game_board.fullCells += 1
        game_board.Display()
        game_status = game_board.Status()
        if game_status != XOBoard.Status.NONE:
            print('The winner is: {}'.format(game_status.name))
            return

if __name__ == '__main__':
    playXOGame()


