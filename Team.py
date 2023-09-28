'''Team module contains the Codegiver and Decoder classes.
These make up the different roles on the red and blue team.'''
from os import system
import sys

class Codegiver:
    '''Codegiver is the class of the person that looks at the board and give a word.
    -team = red or blue team
    -code_word = the new code word each round goes here
    -code_number = the number of cards that the code word is meant for'''
    def __init__(self, team):
        self.code_word = ''
        self.code_number = 0
        self.team = team
        self.skip = 0
        self.create_decoder = 0
        self.game_over = False

    def create_code_word(self):
        '''Tells you which team you are on.
        Asks for a code word and how many cards you are referring to.'''
        if not self.skip:
            print(f"\t\t\t\t\t\t\tThis is team {self.team}")
            self.code_word = input("\t\t\t\t\t\tEnter your Code Word: ")
            while True:
                self.code_number = input("\t\t\t\t\tHow many cards this word is for: ")
                if self.code_number.isdigit():
                    self.code_number = int(self.code_number)
                    break
                else:
                    print("Please enter a valid number.\n")
            self.create_decoder = True
            system("clear")
            input('\nPress "Enter" to continue to the guesser\'s turn: ')
            system("clear")
        else:
            input()


    def __str__(self):
        return f" {self.code_word} {self.code_number}"

class Decoder:
    '''Decoder is the class of the people recieving the word and taking a guess.
    -class_codegiver is used to take either the red or blue team codegiver object.
    -class_board takes the board object
    -team is meant to take a string that is either "red" or "blue"
    -death_card is set to false. If the death card is picked it will change to true and
    end the game though the win.py module'''
    def __init__(self, class_codegiver, class_board, team):
        self.team = team
        self.code_word = class_codegiver.code_word
        self.guesses_left = class_codegiver.code_number
        self.cards = class_board.cards
        self.death_card = False
        self.guess = ''
        self.guess_value = 0

    def take_guess(self):
        '''The decoder takes their guess in this function'''
        # input() is used to pause the game before it continues to the next segment here. The prompt is in board.render
        if self.guess_value > 0:
            input()
        print(f"\t\t\t\t\t\t\t\tTeam {self.team}.")
        print(f"\t\t\t\t\t\t\tThe code word is --{self.code_word.capitalize()}--\n\t\t\t\t\t\t\t\tfor --{self.guesses_left}--\n")

        flag = False
        # while loop is used to check if the guess exists on the board and if it has already been guessed or not.
        while not flag:
            self.guess = input("Enter the word on the card you think this applies to: ").capitalize()
            if self.guess in [card.word for card in self.cards if card.flipped]:
                print("This has already been guessed. Guess again.\n")
                continue
            for card in self.cards:
                if self.guess == card.word:
                    flag = True
                    break
            if not flag:
                print("Please enter a word on one of the cards. Guess again\n")
            if flag:
                break
        system("clear")
    
    def check_guess(self):
        '''There are 4 options.
        1)It is their teams word. 2)It is the other team's word 
        3)It is a nuetral word 4)It is the death card and the game is over.'''
        value = 0
        for card in self.cards:
            if self.guess == card.word:
                card.flipped = True
                if self.team == card.color:
                    value = 1
                elif self.team != card.color and card.color != "yellow" and card.color != "black":
                    value = 2
                elif card.color == "yellow":
                    value = 3
                elif card.color == "black":
                    value = 4
                    self.death_card = True
                break
        if value == 1:
            self.guesses_left -= 1
        else:
            self.guesses_left = 0
        return value
    
    def update_state(self, guessing, codegiver, decoder, red_codegiver, blue_codegiver, board):
        '''Update decoder, check if guessing is still true, and updated codegiver.'''
        # only creates decoder after create_code_word() has been run
        if codegiver.create_decoder:
            decoder = Decoder(codegiver, board, codegiver.team)
            codegiver.create_decoder = False
        guessing = (decoder.guess_value <= 1 and decoder.guesses_left > 0)
        if not guessing:
            # This puts the game through an extra loop which allows render() to print out the non-answer board one time after the turn is over.
            codegiver.skip = 1 if codegiver.skip == 0 else 0
            if codegiver.game_over and not codegiver.skip:
                sys.exit()
            # creates the new codegiver if guessing has become False and the skipped turn is past.
            if not codegiver.skip:
                codegiver = red_codegiver if codegiver == blue_codegiver else blue_codegiver
        return guessing, decoder, codegiver
    