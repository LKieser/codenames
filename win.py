def win_condition(team_color, decoder_object, board_object, Flag):
    if team_color == "blue":
        if decoder_object.game_end:
            print("The game is over!")
            print("Blue picked the death card.")
            print("Red wins! Congratulations!")
            Flag = False
        elif sorted(board_object.guesses[1]) == sorted(board_object.rand_answers[1]):
            print("The game is over!")
            print("Blue Team correctly guessed all of their cards.")
            print("Blue wins! Congratulations!")
            Flag = False
    if team_color == "red":
        if decoder_object.game_end:
            print("The game is over!")
            print("Red picked the death card.")
            print("Blue wins! Congratulations!")
            Flag = False
        elif sorted(board_object.guesses[0]) == sorted(board_object.rand_answers[0]):
            print("The game is over!")
            print("Red Team correctly guessed all of their cards.")
            print("Red wins! Congratulations!")
            Flag = False
    return Flag
