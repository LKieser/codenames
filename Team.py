from Board import Board

class Codegivers:
    def __init__(self, team, code_word = "", code_number = 0):
        self.code_word = code_word 
        self.code_number = code_number
        self.team = team

    def create_code_word(self):
        print(f"\t\t\t\t\t\t\tThis is team {self.team}")
        self.code_word = input("\t\t\t\t\t\tEnter your Code Word: ")
        self.code_number = int(input("\t\t\t\t\tHow many cards this word is for: "))  # need to add input validation for this
        return self.code_word

    def __str__(self):
        return f" {self.code_word} {self.code_number}"

class Decoders(Codegivers):
    def __init__(self, class_Codegivers, team, class_Board, game_end = False):
        # Codegivers.__init__(self, team, code_word, code_number)
        self.team = team
        self.code_word = class_Codegivers.code_word
        self.code_number = class_Codegivers.code_number
        self.guesses = class_Board.guesses
        self.rand_answers = class_Board.rand_answers
        self.game_end = game_end

    def take_guess(self):
        print(f"\t\t\t\t\t\t\t\tTeam {self.team}.")
        print(f"\t\t\t\t\t\t\tThe code word is --{self.code_word.upper()}--\n\t\t\t\t\t\t\t\tfor --{self.code_number}--\n")
        Flag = False
        for i in range(1,self.code_number+1):
            while True:
                guess = input(f"Enter word {i} on the card you think this applies to: ").capitalize()
                # this if statement checks if you are part of the red team which is in 0 or the blue team which is in 1.
                # if you guess is correct for your team's colors, the guess will go into your list.
                if guess in self.rand_answers[0 if self.team == "red" else 1]:
                    self.guesses[0 if self.team == "red" else 1] += [guess]
                    input("\nCorrect!\tPress \"Enter\" to continue: ")
                    break
                # this next statement check if the word belongs to the other team. It will then put the word in the other team's words.
                elif guess in self.rand_answers[1 if self.team == "red" else 0]:
                    self.guesses[1 if self.team == "red" else 0] += [guess]
                    input("\nThat is the other team's word! Your turn is over.\tPress \"Enter\" to continue: ")
                    Flag = True
                    break
                # adds the nuetral words
                elif guess in self.rand_answers[2]:
                    self.guesses[2] += [guess]
                    input("\nThat is a nuetral word. Your turn is over.\tPress \"Enter\" to continue: ")
                    Flag = True
                    break
                elif guess in self.rand_answers[3]:
                    self.guesses[3] += [guess]
                    input("\nThat was the death card! Game Over!\tPress \"Enter\" to continue: ")
                    Flag = True
                    self.game_end = True
                    break
                else:
                    print("\nYou did not enter a valid word for this game. Try again.")
            if Flag:
                break
