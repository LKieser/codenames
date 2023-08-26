from random import choice
from termcolor import colored
from Word_list import rand_words

class Board:
    def __init__(self, rand_answers = [], guesses = [[],[],[],[]], first_player=""):
        self.rand_words = rand_words
        self.rand_answers = rand_answers
        self.guesses = guesses
        self.first_player = first_player

    
    def create_each_deck(self):
        # creates the first turn cards. Weeds out all duplicate words
        first = []
        for i in range(9):
            while True:
                word = choice(rand_words)
                if word in [a for a in first]:
                    continue
                else:
                    first += [word]
                    break
        # creates the second turn cards. Weeds out all duplicate words
        second = []
        for i in range(8):
            while True:
                word = choice(rand_words)
                if word in [a for a in first] or word in [b for b in second]:
                    continue
                else:
                    second += [word]
                    break
        # creates the Neutral Cards
        nuetral = []
        for i in range(7):
            while True:
                word = choice(rand_words)
                if word in [a for a in first] or word in [b for b in second] or word in [c for c in nuetral]:
                    continue
                else:
                    nuetral += [word]
                    break

        # Creates the Death card
        while True:
            word = choice(rand_words)
            if word in [a for a in first] or word in [b for b in second] or word in [c for c in nuetral]:
                continue
            else:
                death = [word]
                break
        
        
        # choose colors for each list
        chooser = [first, second]
        lst = [0,1]
        x = choice(lst)             # chooses blue or red
        y = 1 if x != 1 else 0
        red = chooser[x]
        blue = chooser[y]
        
        self.first_player = "red" if red == first else "blue" # creates a string for the player that goes first

        self.rand_answers = [red, blue, nuetral, death]  # creates a list with each of the different colors in it.

        return f"\t\t\t\t\t\t\t--{self.first_player} goes first--"
    
    def board_row(self,a,b,c,d,e):
        x = f'''
 ________________________   ________________________   ________________________   ________________________   ________________________    
|                        | |                        | |                        | |                        | |                        |
|                        | |                        | |                        | |                        | |                        |
|        {a:25}    | |      {b:25}      | |        {c:25}    | |        {d:25}    | |        {e:25}    |
|                        | |                        | |                        | |                        | |                        |
|________________________| |________________________| |________________________| |________________________| |________________________|
'''
        
        return x
    
    def answer_color(self,A):
        if self.rand_words[A] in self.rand_answers[0]:
            color = "red"
            if self.rand_words[A] in self.guesses[0]:
                attr = "reverse"
            else:
                attr = "bold"
        elif self.rand_words[A] in self.rand_answers[1]:
            color = "blue"
            if self.rand_words[A] in self.guesses[1]:
                attr = "reverse"
            else:
                attr = "bold"
        elif self.rand_words[A] in self.rand_answers[2]:
            color = "grey"
            if self.rand_words[A] in self.guesses[2]:
                attr = "reverse"
            else:
                attr = "bold"
        else:
            color = "yellow"
            if self.rand_words[A] in self.guesses[3]:
                attr = "reverse"
            else:
                attr = "bold"


        return colored(self.rand_words[A], color, attrs=[attr] )

    def answers_board(self):
        for i in range(0,25,5):
            a = self.answer_color(i)  # creates 5 rows of 5 cards each
            b = self.answer_color(i+1)
            c = self.answer_color(i+2)
            d = self.answer_color(i+3)
            e = self.answer_color(i+4)
            print(self.board_row(a,b,c,d,e))

    def all_color(self, A):
        return colored(self.rand_words[A], "red" if self.rand_words[A] in self.guesses[0] 
                       else "blue" if self.rand_words[A] in self.guesses[1] 
                       else "black" if self.rand_words[A] in self.guesses[2] 
                       else "yellow" if self.rand_words[A] in self.guesses[3] 
                       else "light_grey", attrs=["bold"] )
    
    def all_board(self):
        for i in range(0,25,5):
            a = self.all_color(i)  # creates 5 rows of 5 cards each
            b = self.all_color(i+1)
            c = self.all_color(i+2)
            d = self.all_color(i+3)
            e = self.all_color(i+4)
            print(self.board_row(a,b,c,d,e))

    
    def __str__(self):
        return "You didn't mean to print this."
    
board = Board()

board.all_board()