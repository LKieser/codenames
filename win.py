'''Module contains the check_win() function that will be plugged into
the main.py module and end the game if the conditions are met.'''

def check_win(decoder_object, board_object):
    '''Function ends the game on a few conditions:
    1) If Blue or Red pick the death card the game will end.
    2) If either team gets their entire word set the game will end.'''
    color = ["Blue","Red"]
    game_over = False

    if decoder_object.death_card:
        print(f"{decoder_object.team} picked the death card.")
        print("The game is over!")
        print(f"{color[0] if decoder_object.team.capitalize() == color[1] else color[1]} wins! Congratulations!")
        game_over = True

    # This runs twice in order to check the red and the blue decks
    for i in color:
        all_team_color_cards = [card.word for card in board_object.cards if card.color.capitalize() == i]
        all_flipped_team_color_cards = [card.word for card in board_object.cards if card.flipped and card.color.capitalize() == i]

        if all_team_color_cards == all_flipped_team_color_cards:
            print("The game is over!")
            print(f"{i} Team correctly guessed all of their cards.")
            print(f"{i} wins! Congratulations!")
            game_over = True
    return game_over
