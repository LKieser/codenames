"""-Import the system to allow the terminal to be cleared using system("clear").
-Import The Board to get the class that prints the board in terminal.
-Import Codegivers and Decoders to get classess for the two different types of players.
-Import win_condition function to be exectued
and end the game when the win conditions have been met."""
from os import system
from Board import Board
from Team import Codegivers, Decoders
from win import win_condition


def main():
    """main function contains entire game play"""
    # This section creates the board and the blue and red team codegivers.
    board = Board()
    red_codegiver = Codegivers("red")
    blue_codegiver = Codegivers("blue")
    flag = True

    print(board.create_each_deck())
    input('\nPress "Enter" when you are ready to begin the game: ')
    while True:
        # this section clears the terminal and then ask the codegiver to give their word
        system("clear")
        input("\nIt is now the Codegivers turn.\nWARNING: all word guessers must look away from the screen!\n\nPress \"Enter\" when you are ready: ")
        system("clear")
        board.answers_board()
        if board.first_player == "red":
            red_codegiver.create_code_word()
        else:
            blue_codegiver.create_code_word()

        system("clear")
        input('\nPress "Enter" to continue to the guesser\'s turn: ')
        system("clear")
        # Ask for a guess from the red decoders
        if board.first_player == "red":
            # creates the decoder object again to update it
            red_decoder = Decoders(red_codegiver, "red", board)
            board.all_board()
            red_decoder.take_guess()
            system("clear")
            # check for win
            if not win_condition("red", red_decoder, board, flag):
                board.all_board()
                break
            board.all_board()
            input('\nThis is the current board. Press "Enter" to continue the game.')
        # ask for a guess from the blue decoders
        else:
            # creates the decoder object again to update it
            blue_decoder = Decoders(blue_codegiver, "blue", board)
            board.all_board()
            blue_decoder.take_guess()
            system("clear")
            # check for win
            if not win_condition("blue", blue_decoder, board, flag):
                board.all_board()
                break
            board.all_board()
            input('\nThis is the current board. Press "Enter" to continue the game.')

        # this section ask the other codegiver to give their word
        system("clear")
        input("\nIt is now the Codegivers turn.\nWARNING: all word guessers must look away from the screen!\n\nPress \"Enter\" when you are ready: ")
        system("clear")
        board.answers_board()
        # this one is for the second turn so it is backwards from the first one
        if board.first_player == "blue":
            red_codegiver.create_code_word()
        else:
            blue_codegiver.create_code_word()

        system("clear")
        input('\nPress "Enter" to continue to the guesser\'s turn: ')
        system("clear")
        # Ask for a guess from the red decoders
        if board.first_player == "blue":
            # creates the decoder object again to update it
            red_decoder = Decoders(red_codegiver, "red", board)
            board.all_board()
            red_decoder.take_guess()
            system("clear")
            if not win_condition("blue", blue_decoder, board, flag):
                board.all_board()
                break
            board.all_board()
            input('\nThis is the current board. Press "Enter" to continue the game.')
        # ask for a guess from the blue decoders
        else:
            # creates the decoder object again to update it
            blue_decoder = Decoders(blue_codegiver, "blue", board)
            board.all_board()
            blue_decoder.take_guess()
            system("clear")
            if not win_condition("red", red_decoder, board, flag):
                board.all_board()
                break
            board.all_board()
            input('\nThis is the current board. Press "Enter" to continue the game.')


if __name__ == "__main__":
    main()
