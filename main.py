"""Main module contains only the main() function 
which combines all of the other modules to create the game play."""
from os import system
from board import Board
from Team import Codegiver, Decoder
from win import win_condition


def main():
    """main function contains entire game play"""
    # This section creates the board and the blue and red team codegiver.
    board = Board()
    red_codegiver = Codegiver("red")
    blue_codegiver = Codegiver("blue")

    print(board.output(2))
    input('\nPress "Enter" when you are ready to begin the game: ')
    while True:
        # this section clears the terminal and then ask the codegiver to give their word
        system("clear")
        input("\nIt is now the Codegiver turn.\nWARNING: all word guessers must look away from the screen!\n\nPress \"Enter\" when you are ready: ")
        system("clear")
        print(board.output(1))

        codegiver = red_codegiver if board.up_next == "red" else blue_codegiver
        codegiver.create_code_word()

        system("clear")
        input('\nPress "Enter" to continue to the guesser\'s turn: ')
        system("clear")
        # Ask for a guess from the decoder
        decoder = Decoder(codegiver, board, "red")
        print(board.output(2))
        decoder.take_guess()
        system("clear")
        # check for win
        win_condition(decoder, board)
        print(board.output(2))
        input('\nThis is the current board. Press "Enter" to continue the game.')

        if board.up_next == "red":
            board.up_next = "blue"
        else:
            board.up_next = "red"


if __name__ == "__main__":
    main()
