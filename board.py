'''Card class contains the attributes for each individual card. 
The Board class creates the deck and uses the Card class to print 
out two boards: The answer board and the common board.'''
import random
from termcolor import colored

class Card:
    '''Card is used by the board to store the word, color, and if it has been flipped of each of the individual 25 words'''
    def __init__(self, word: str, color: str):
        self.word = word
        self.color = color
        self.flipped = False

class Board:
    '''creates the deck of cards in the __init__ function and 
    then prints the board though the output function'''
    def __init__(self):
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
        self.up_next = random.choice(["red", "blue"])
        cards.append(Card(lines.pop().replace("\n", ""), self.up_next))

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

    def output(self, n):
        '''This function is needed to have two boards to print. A board for the codegiver and a board for the decoder'''
        # n = 1 for answer board and 2 for everyone's board
        str = ""
        row = []
        for i, card in zip(range(len(self.cards)), self.cards):
            # colors the card if it is the answer board or if it is a flipped card. It highlights it if it is in the answer board and flipped
            row.append(colored(card.word, card.color if n == 1 else card.color if n == 2 and card.flipped else 'light_grey', 'on_black', ["reverse"] if card.flipped and n == 1 else ["bold"]))
            if ((i+1) % 5) == 0:
                str += self.row_string(row)
                row.clear()
        return str

    def __str__(self):
        return "temporary"
