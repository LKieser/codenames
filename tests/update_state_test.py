'''This module runs tests for the three functions in the update stare section of the game loop:
1) check_guess 2) check_win 3) update_state'''
import sys
sys.path.append("..")
from game import Game



game = Game()

class TestCheckGuess:
    'Check_guess is responsible for checking the guessed word and identifying which deck it belongs to.'
    def test_correct_guess(self):
        'test if a guess can equal a word in cards resulting in card.flipped set equal to True'
        # Create a correct guess
        game.guess = game.board.cards[0].word

        game.check_guess()


        assert game.board.cards[0].flipped is True

    def test_guessed_correct_word(self):
        'test if the guessed word belongs to the team that picked it'
        # game.guess is set equal to the first word that has the same color as the teams color
        game.guess = [card.word for card in game.board.cards if card.color == game.team][0]

        game.check_guess()

        assert game.guess_value == 1

    def test_guessed_opponents_word(self):
        'test if the guessed word belongs to the other team'
        game.team = "red"
        # game.guess is the first word thats color is the opposite teams word
        game.guess = [card.word for card in game.board.cards if card.color == "blue"][0]

        game.check_guess()

        assert game.guess_value == 2

    def test_guessed_neutral_word(self):
        'test if the guessed word belongs to the neutral stack'
        # game.guess is the first neutral word
        game.guess = [card.word for card in game.board.cards if card.color == "yellow"][0]

        game.check_guess()

        assert game.guess_value == 3

    def test_guessed_death_word(self):
        'test if the guessed word is the death card'
        # game.guess is the death word
        game.guess = [card.word for card in game.board.cards if card.color == "black"][0]

        game.check_guess()

        assert game.guess_value == 4

    def test_code_number_decrease(self):
        'test if code_number gets decreased when the correct answer is guessed'
        game.code_number = 3
        game.guess = ""
        # 1 means this is the correct answer
        game.guess_value = 1

        game.check_guess()

        assert game.code_number == 2

    def test_code_number_reset(self):
        'test if code_number is set to zero when the correct answer is not guessed'
        game.code_number = 3
        game.guess = ""
        # 2 means not the correct answer
        game.guess_value = 2

        game.check_guess()

        assert game.code_number == 0


class TestCheckWin:
    '''Check_win is responsible for assigning a winner if the death card 
    is picked or if the entire deck has been flipped'''
    def test_winner_and_game_over_for_death_card(self):
        'test if winner_color is the opposite team and game_over is True'
        game.winner_color = "none"
        game.guess_value = 4
        game.team = "blue"

        game.check_win()

        assert game.winner_color == 'red'
        assert game.game_over is True

    def test_winner_for_death_card(self):
        'test if when team is "red", winner_color is "blue"'
        game.winner_color = "none"
        game.guess_value = 4
        game.team = "red"

        game.check_win()

        assert game.winner_color == 'blue'

    def test_red_complete_deck(self):
        'test if when all red cards are flipped, winner_color = red and game_over is True'
        game.winner_color = "none"
        game.game_over = False
        # make all red cards guessed
        for card in game.board.cards:
            if card.color == 'red':
                card.flipped = True

        game.check_win()

        assert game.winner_color == 'red'
        assert game.game_over is True

    def test_blue_complete_deck(self):
        'test if when all blue cards are flipped, winner_color = blue and game_over is True'
        game.winner_color = "none"
        game.game_over = False
        # make all blue cards guessed
        for card in game.board.cards:
            if card.color == 'blue':
                card.flipped = True

        game.check_win()

        assert game.winner_color == 'blue'
        assert game.game_over is True

class TestUpdateState:
    '''Update_state sets guessing to True or False, then sets skip True first then False,
    and finally, switches the team color and resets guess_value to zero'''
    def test_guessing_is_true_under_right_conditions(self):
        'If these three variables are as they are set here, guessing should be True'
        game.guess_value = 1
        game.code_number = 1
        game.game_over = False

        game.update_state()

        assert game.guessing is True

    def test_guessing_is_false_when_game_over_is_true(self):
        'If game_over is True, guessing should be False'
        game.guess_value = 1
        game.code_number = 1
        game.game_over = True
        # need skip to be True so that self.guessing is not reset to True before test
        game.skip = True

        game.update_state()

        assert game.guessing is False

    def test_guessing_is_false_when_code_number_is_zero(self):
        'If code_number is 0, guessing should be False'
        game.guess_value = 1
        game.code_number = 0
        game.game_over = False
        # need skip to be True so that self.guessing is not reset to True before test
        game.skip = True

        game.update_state()

        assert game.guessing is False

    def test_guessing_is_false_when_guess_value_is_greater_than_one(self):
        'If guess_value is more than one, guessing should be False'
        game.guess_value = 2
        game.code_number = 1
        game.game_over = False
        # need skip to be True so that self.guessing is not reset to True before test
        game.skip = True

        game.update_state()

        assert game.guessing is False

    def test_skip_is_true_when_first_guessing_is_false(self):
        'When guessing is false and skip is false, skip should be changed to True'
        game.skip = False

        game.update_state()

        assert game.skip is True

    def test_skip_is_false_when_second_guessing_is_false(self):
        'When guessing is false and skip is True, skip should be changed to False'
        game.skip = True

        game.update_state()

        assert game.skip is False

    def test_skip_is_true_sets_guessing_to_true(self):
        'When skip is True, guessing should be set equal to True'
        # Set skip to false here as function will change it to True
        game.skip = False

        game.update_state()

        assert game.guessing is True

    def test_skip_is_false_so_team_red_goes_blue_and_guess_value_reset(self):
        'When skip is False, the team should be switched and the guess_value reset'
        # Set skip to True so that function will change it to False for the test
        game.skip = True
        game.team = 'red'
        game.guess_value = 1

        game.update_state()

        assert game.team == 'blue'
        assert game.guess_value == 0

    def test_skip_is_false_so_team_blue_goes_red_and_guess_value_reset(self):
        'When skip is False, the team should be switched and the guess_value reset'
        # Set skip to True so that function will change it to False for the test
        game.skip = True
        game.team = 'blue'
        game.guess_value = 1

        game.update_state()

        assert game.team == 'red'
        assert game.guess_value == 0
