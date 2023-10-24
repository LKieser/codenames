'''Card class contains the attributes for each individual card. 
The Board class creates the deck and uses the Card class to print the board.'''
import random
from termcolor import colored

class Card:
    '''Card is used by the board to store the word, color, and if it has been flipped of each of the individual 25 words'''
    def __init__(self, word: str, color: str):
        self.word = word
        self.color = color
        self.flipped = False

class Board:
    '''Creates the deck of cards in the __init__ function. 
    Render prints the board and is the function that is included in the main game loop.'''
    def __init__(self, up_first):
        self.up_first = up_first
        cards = []
        with open("code_names.txt", "r") as f:
            lines = f.readlines()

        random.shuffle(lines)

        for _ in range(8):
            cards.append(Card(lines.pop().replace("\n", ""), "red"))
            cards.append(Card(lines.pop().replace("\n", ""), "blue"))

        for _ in range(7):
            cards.append(Card(lines.pop().replace("\n", ""), "yellow"))

        cards.append(Card(lines.pop().replace("\n", ""), "black"))
        cards.append(Card(lines.pop().replace("\n", ""), self.up_first))

        random.shuffle(cards)
        self.cards = cards

    def row_string(self, row):
        '''A single card row that is printed five times to create the board'''
        x = f'''
 ________________________   ________________________   ________________________   ________________________   ________________________    
|                        | |                        | |                        | |                        | |                        |
|                        | |                        | |                        | |                        | |                        |
|       {row[0]:35}| |     {row[1]:35}  | |       {row[2]:35}| |       {row[3]:35}| |       {row[4]:35}|
|                        | |                        | |                        | |                        | |                        |
|________________________| |________________________| |________________________| |________________________| |________________________|
'''
        return x

    def render(self, show_answers):
        '''This function is needed to have two boards to print. A board for the codegiver and a board for the decoder'''
        # show_answers is True for the answer board and false for everyone's board
        str = ""
        row = []
        for i, card in zip(range(len(self.cards)), self.cards):
            # colors the card if it is the answer board or if it is a flipped card.
            if show_answers or (not show_answers and card.flipped):
                #  It highlights it if it is in the answer board and flipped
                if show_answers and card.flipped:
                    row.append(colored(card.word, card.color, 'on_black', ['reverse']))
                # It makes all of the other cards bold
                else:
                    row.append(colored(card.word, card.color, 'on_black', ['bold']))
            else:
                row.append(colored(card.word, 'light_grey', 'on_black', ['bold']))

            if ((i+1) % 5) == 0:
                str += self.row_string(row)
                row.clear()
        return print(str)
    