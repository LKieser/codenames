'''Module contains the win condition function that will be plugged into
the main.py module.'''
def win_condition(team_color, decoder_object, board_object, flag):
    '''Function ends the game on a few conditions:
    1) If Blue or Red pick the death card the game will end.
    2) If either team gets their entire word set the game will end.'''
    if team_color == "blue":
        if decoder_object.game_end:
            print("The game is over!")
            print("Blue picked the death card.")
            print("Red wins! Congratulations!")
            flag = False
        elif sorted(board_object.guesses[1]) == sorted(board_object.rand_answers[1]):
            print("The game is over!")
            print("Blue Team correctly guessed all of their cards.")
            print("Blue wins! Congratulations!")
            flag = False
    if team_color == "red":
        if decoder_object.game_end:
            print("The game is over!")
            print("Red picked the death card.")
            print("Blue wins! Congratulations!")
            flag = False
        elif sorted(board_object.guesses[0]) == sorted(board_object.rand_answers[0]):
            print("The game is over!")
            print("Red Team correctly guessed all of their cards.")
            print("Red wins! Congratulations!")
            flag = False
    return flag
