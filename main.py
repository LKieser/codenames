"""Main module contains only the main() function 
which combines all of the other modules to create the game play."""
from board import Board
from Team import Codegiver, Decoder
from win import check_win


def main():
    """main function contains entire game play"""
    # This section creates the board and the blue and red team codegiver.
    board = Board()
    red_codegiver = Codegiver("red")
    blue_codegiver = Codegiver("blue")
    # initial codegiver and decoder
    codegiver = red_codegiver if board.up_next == "red" else blue_codegiver
    decoder = Decoder(codegiver, board, codegiver.team)
    guessing = False
    # Initial board.
    board.render(True, codegiver.skip, decoder.guess_value,board, codegiver.game_over)
    input('\nPress "Enter" when you are ready to begin the game: ')
    while True:
        board.render(guessing, codegiver.skip, decoder.guess_value, board, codegiver.game_over)
        # Process input.
        if guessing:
            decoder.take_guess()
        else:
            codegiver.create_code_word()

        # Update state
        if guessing:
            decoder.guess_value = decoder.check_guess()
            codegiver.game_over = check_win(decoder, board)
        guessing, decoder, codegiver = decoder.update_state(guessing, codegiver, decoder, red_codegiver, blue_codegiver, board)

if __name__ == "__main__":
    main()
