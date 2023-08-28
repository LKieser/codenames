'''Team module contains the Codegiver and Decoder classes.
These make up the different roles on the red and blue team.'''
class Codegivers:
    '''Codegivers is the class of the person that looks at the board and give a word.
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
        # need to add input validation for both of these
        self.code_word = input("\t\t\t\t\t\tEnter your Code Word: ")
        self.code_number = int(input("\t\t\t\t\tHow many cards this word is for: "))
        return self.code_word

    def __str__(self):
        return f" {self.code_word} {self.code_number}"

class Decoders:
    '''Decoders is the class of the people recieving the word and taking a guess.
    -class_codegivers is used to take either the red or blue team codegiver object.
    -team is meant to take a string that is either "red" or "blue"
    -class_board takes the board object
    -game_end is set to false. If the death card is picked it will change to true and
    end the game though the win.py module'''
    def __init__(self, class_codegivers, team, class_board, game_end = False):
        self.team = team
        self.code_word = class_codegivers.code_word
        self.code_number = class_codegivers.code_number
        self.guesses = class_board.guesses
        self.rand_answers = class_board.rand_answers
        self.game_end = game_end

    def take_guess(self):
        '''This is the gameplay of the Decoder. Once they type in a word there are 4 options.
        1)It is their teams word. 2)It is the other team's word 
        3)It is a nuetral word 4)It is the death card and the game is over.'''
        print(f"\t\t\t\t\t\t\t\tTeam {self.team}.")
        print(f"\t\t\t\t\t\t\tThe code word is --{self.code_word.upper()}--\n\t\t\t\t\t\t\t\tfor --{self.code_number}--\n")
        flag = False
        for i in range(1,self.code_number+1):
            while True:
                guess = input(f"Enter word {i} on the card you think this applies to: ").capitalize()
                # this if statement checks if you are part of the red team which is in 0 or the blue team which is in 1.
                # if your guess is correct for your team's colors, the guess will go into your list.
                if guess in self.rand_answers[0 if self.team == "red" else 1]:
                    self.guesses[0 if self.team == "red" else 1] += [guess]
                    input("\nCorrect!\tPress \"Enter\" to continue: ")
                    break
                # this next statement checks if the word belongs to the other team. 
                # It will then put the word in the other team's words.
                elif guess in self.rand_answers[1 if self.team == "red" else 0]:
                    self.guesses[1 if self.team == "red" else 0] += [guess]
                    input("\nThat is the other team's word! Your turn is over.\tPress \"Enter\" to continue: ")
                    flag = True
                    break
                # adds the nuetral words
                elif guess in self.rand_answers[2]:
                    self.guesses[2] += [guess]
                    input("\nThat is a nuetral word. Your turn is over.\tPress \"Enter\" to continue: ")
                    flag = True
                    break
                # if it is the death card the game will come to an end
                elif guess in self.rand_answers[3]:
                    self.guesses[3] += [guess]
                    input("\nThat was the death card! Game Over!\tPress \"Enter\" to continue: ")
                    flag = True
                    self.game_end = True
                    break
                else:
                    print("\nYou did not enter a valid word for this game. Try again.")
            if flag:
                break
