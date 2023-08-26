"""Random is needed to randomize which words are picked for the game."""
from random import randint
from linecache import getline

with open("code_names.txt", "r", encoding="utf-8") as words:
    rand_words = []
    for j in range(25):
        while True:
            word = getline("code_names.txt", randint(1, 673)).replace("\n", "")
            if word in [a for a in rand_words]:
                continue
            elif len(word) > 12:
                continue
            else:
                rand_words += [word]
                break
