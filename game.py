'''Game module contains all of the functions used in the main game loop'''
from os import system
from board import Board
import random

class Game:
    '''Initialize the game. This will only run once.
    Contains the Codegiver functions and Decoder functions.'''
    def __init__(self):
        self.team = random.choice(["red", "blue"])
        self.board = Board(up_first=self.team)
        self.code_word = ''
        self.code_number = 0
        # skip is needed to override the stateful loop based on whether guessing is True or False.
        # This allows render() to print out the non-answer board one more time before the answer board is printed for the Codegiver.
        self.skip = False 
        self.game_over = False
        self.guess = ''
        self.guess_value = 0
        self.guessing = False
        self.winner_color = ''

    def render(self, guessing = None):
        '''This function is used in the game loop and prints either the decoder board or the codegiver board'''
        if guessing is None:
            guessing = self.guessing
        
        # codegiver
        if not guessing:
            system("clear")
            input("\nIt is now the Codegiver's turn.\nWARNING: all word guessers must look away from the screen!\n\nPress \"Enter\" when you are ready: ")
            system("clear")

        # print board
        self.board.render(show_answers = not guessing)

        # decoder
        if guessing:
            if self.guess_value == 1:
                print("\nCorrect!\tPress \"Enter\" to continue: ")
            if self.guess_value == 2:
                print("\nThat is the other team's word! Your turn is over.\tPress \"Enter\" to continue: ")
            if self.guess_value == 3:
                print("\nThat is a neutral word. Your turn is over.\tPress \"Enter\" to continue: ")
            if self.game_over:
                # death card
                if self.guess_value == 4:
                    print(f"\n{self.team} picked the death card.")
                    print("The game is over!")
                    print(f"{self.winner_color} wins! Congratulations!")
                # all cards guessed
                else:
                    print("\nThe game is over!")
                    print(f"{self.winner_color} team correctly guessed all of their cards.")
                    print(f"{self.winner_color} wins! Congratulations!")


    def create_code_word(self):
        '''Used in the game loop to ask the codegiver for their codeword and the number of cards it applies to.'''
        print(f"\t\t\t\t\t\t\tThis is team {self.team}")
        self.code_word = input("\t\t\t\t\t\tEnter your Code Word: ")
        while True:
            self.code_number = input("\t\t\t\t\tHow many cards this word is for: ")
            if self.code_number.isdigit():
                self.code_number = int(self.code_number)
                break
            else:
                print("Please enter a valid number.\n")
        system("clear")
        input('\nPress "Enter" to continue to the guesser\'s turn: ')
        system("clear")
        

    def take_guess(self):
        '''The decoder takes their guess in this function'''
        # input() is used to pause the game before it continues to the next segment here. The prompt is in board.render
        if self.guess_value > 0:
            input()
        print(f"\t\t\t\t\t\t\t\tTeam {self.team}.")
        print(f"\t\t\t\t\t\t\tThe code word is --{self.code_word.capitalize()}--\n\t\t\t\t\t\t\t\tfor --{self.code_number}--\n")

        # while loop is used to check if the guess exists on the board and if it has already been guessed or not.
        while True:
            self.guess = input("Enter the word on the card you think this applies to: ").capitalize()
            if self.guess in [card.word for card in self.board.cards if card.flipped]:
                print("This has already been guessed. Guess again.\n")
            elif self.guess in [card.word for card in self.board.cards]:
                break
            else:
                print("Not on board. Please enter a word on one of the cards. Guess again\n")
        system("clear")
        
    
    def check_guess(self):
        '''There are 4 options.
        1)It is their teams word. 2)It is the other team's word 
        3)It is a neutral word 4)It is the death card and the game is over.'''
        for card in self.board.cards:
            if self.guess == card.word:
                card.flipped = True
                if self.team == card.color:
                    self.guess_value = 1
                elif self.team != card.color and card.color != "yellow" and card.color != "black":
                    self.guess_value = 2
                elif card.color == "yellow":
                    self.guess_value = 3
                elif card.color == "black":
                    self.guess_value = 4
                break
        if self.guess_value == 1:
            self.code_number -= 1
        else:
            self.code_number = 0

    def check_win(self):
        '''Function ends the game on a few conditions:
        1) If Blue or Red pick the death card the game will end.
        2) If either team gets their entire word set the game will end.'''
        color = ["blue","red"]

        if self.guess_value == 4:
            self.winner_color = 'red' if self.team == 'blue' else 'blue'
            self.game_over = True

        # This runs twice in order to check the red and the blue decks
        for i in color:
            all_team_color_cards = [card.word for card in self.board.cards if card.color == i]
            all_flipped_team_color_cards = [card.word for card in self.board.cards if card.flipped and card.color == i]

            if all_team_color_cards == all_flipped_team_color_cards:
                self.winner_color = i
                self.game_over = True

    def update_state(self):
        '''Check if guessing is still true.
        When guessing is no longer true, end game if game is over or update the team color.'''
        self.guessing = (self.guess_value <= 1 and self.code_number > 0) and not self.game_over
        if not self.guessing:
            self.skip = False if self.skip else True
            if self.skip:
                self.guessing = True
            # Switches the team color if guessing has become False and the skipped turn is past.
            if not self.skip:
                self.team = "red" if self.team != "red" else "blue"
                self.guess_value = 0
