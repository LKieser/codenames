'''Module contains the win condition function that will be plugged into
the main.py module and end the game if the conditions are met.'''
import sys

def win_condition(decoder_object, board_object):
    '''Function ends the game on a few conditions:
    1) If Blue or Red pick the death card the game will end.
    2) If either team gets their entire word set the game will end.'''
    color = ["Blue","Red"]

    if decoder_object.death_card:
        print("The game is over!")
        print(f"{decoder_object.team} picked the death card.")
        print(f"{color[0] if decoder_object.team.capitalize() == color[1] else color[1]} wins! Congratulations!")
        print(board_object.output(1))
        sys.exit()

    # This runs twice in order to check the red and the blue decks
    for i in color:
        all_team_color_cards = [card.word for card in board_object.cards if card.color.capitalize() == i]
        all_flipped_team_color_cards = [card.word for card in board_object.cards if card.flipped and card.color.capitalize() == i]

        if all_team_color_cards == all_flipped_team_color_cards:
            print("The game is over!")
            print(f"{i} Team correctly guessed all of their cards.")
            print(f"{i} wins! Congratulations!")
            print(board_object.output(1))
            sys.exit()
