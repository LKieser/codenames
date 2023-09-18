'''Team module contains the Codegiver and Decoder classes.
These make up the different roles on the red and blue team.'''
class Codegiver:
    '''Codegiver is the class of the person that looks at the board and give a word.
    -team = red or blue team
    -code_word = the new code word each round goes here
    -code_number = the number of cards that the code word is meant for'''
    def __init__(self, team, code_word = "", code_number = 0):
        self.code_word = code_word
        self.code_number = code_number
        self.team = team

    def create_code_word(self):
        '''Tells you which team you are on.
        Asks for a code word and how many cards you are referring to.'''
        print(f"\t\t\t\t\t\t\tThis is team {self.team}")
        self.code_word = input("\t\t\t\t\t\tEnter your Code Word: ")
        while True:
            self.code_number = input("\t\t\t\t\tHow many cards this word is for: ")
            if self.code_number.isdigit():
                self.code_number = int(self.code_number)
                break
            else:
                print("Please enter a valid number.\n")


    def __str__(self):
        return f" {self.code_word} {self.code_number}"

class Decoder:
    '''Decoder is the class of the people recieving the word and taking a guess.
    -class_codegiver is used to take either the red or blue team codegiver object.
    -class_board takes the board object
    -team is meant to take a string that is either "red" or "blue"
    -death_card is set to false. If the death card is picked it will change to true and
    end the game though the win.py module'''
    def __init__(self, class_codegiver, class_board, team, death_card = False):
        self.team = team
        self.code_word = class_codegiver.code_word
        self.code_number = class_codegiver.code_number
        self.cards = class_board.cards
        self.death_card = death_card

    def take_guess(self):
        '''This is the gameplay of the Decoder. Once they type in a word there are 4 options.
        1)It is their teams word. 2)It is the other team's word 
        3)It is a nuetral word 4)It is the death card and the game is over.'''
        print(f"\t\t\t\t\t\t\t\tTeam {self.team}.")
        print(f"\t\t\t\t\t\t\tThe code word is --{self.code_word.capitalize()}--\n\t\t\t\t\t\t\t\tfor --{self.code_number}--\n")
        for i in range(1,self.code_number+1):
            flag = False
            # while loop is used to check if the guess exists on the board and if it has already been guessed or not.
            while not flag:
                guess = input(f"Enter word {i} on the card you think this applies to: ").capitalize()
                if guess in [card.word for card in self.cards if card.flipped]:
                    print("This has already been guessed. Guess again.\n")
                    continue
                for card in self.cards:
                    if guess == card.word:
                        flag = True
                        break
                if not flag:
                    print("Please enter a word on one of the cards. Guess again\n")
                
            flag = False
            for card in self.cards:
                if guess == card.word:
                    card.flipped = True
                    if self.team == card.color:
                        input("\nCorrect!\tPress \"Enter\" to continue: ")
                    elif self.team != card.color and card.color != "yellow" and card.color != "black":
                        input("\nThat is the other team's word! Your turn is over.\tPress \"Enter\" to continue: ")
                        flag = True
                    elif card.color == "yellow":
                        input("\nThat is a nuetral word. Your turn is over.\tPress \"Enter\" to continue: ")
                        flag = True
                    elif card.color == "black":
                        input("\nThat was the death card! Game Over!\tPress \"Enter\" to continue: ")
                        self.death_card = True
                        flag = True

            if flag:
                break
