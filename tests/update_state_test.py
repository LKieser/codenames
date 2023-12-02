'''This module runs tests for the three functions in the update stare section of the game loop:
1) check_guess 2) check_win 3) update_state'''
import sys
sys.path.append("..")
from game import Game


class TestCheckGuess:
    'Check_guess is responsible for checking the guessed word and identifying which deck it belongs to.'
    def test_correct_guess(self):
        'Test if flipped starts as false and ends as true.'
        'Also check if guess is correct and code_number to have 1 subtracted from it'
        game = Game()
        # Create a code_number to see the change that should happen
        game.code_number = 3
        # Create a correct guess for the correct team
        game.guess = [card.word for card in game.board.cards if card.color == game.team][0]

        assert [card.flipped for card in game.board.cards if card.word == game.guess][0] is False

        game.check_guess()

        assert [card.flipped for card in game.board.cards if card.word == game.guess][0] is True
        assert game.guess_value == 1
        assert game.code_number == 2

    def test_guessed_opponents_word(self):
        'Test if flipped starts as false and ends as true.'
        'Also check if guess is the other teams and code_number is reset'
        game = Game()

        game.team = "red"
        game.code_number = 3
        # game.guess is the first word that has the color of the opposite teams word
        game.guess = [card.word for card in game.board.cards if card.color == "blue"][0]

        assert [card.flipped for card in game.board.cards if card.word == game.guess][0] is False

        game.check_guess()

        assert [card.flipped for card in game.board.cards if card.word == game.guess][0] is True
        assert game.guess_value == 2
        assert game.code_number == 0

    def test_guessed_neutral_word(self):
        'Test if flipped starts as false and ends as true.'
        'Also check if guess is neutral and code_number is reset'
        # game.guess is the first neutral word
        game = Game()
        game.code_number = 3
        # game.guess is the first word that is a neutral word
        game.guess = [card.word for card in game.board.cards if card.color == "yellow"][0]

        assert [card.flipped for card in game.board.cards if card.word == game.guess][0] is False

        game.check_guess()

        assert [card.flipped for card in game.board.cards if card.word == game.guess][0] is True
        assert game.guess_value == 3
        assert game.code_number == 0

    def test_guessed_death_word(self):
        'Test if flipped starts as false and ends as true.'
        'Also check if guess is the death word and code_number is reset'
        game = Game()
        game.code_number = 3
        # game.guess is the first word that is the death word
        game.guess = [card.word for card in game.board.cards if card.color == "black"][0]

        assert [card.flipped for card in game.board.cards if card.word == game.guess][0] is False

        game.check_guess()

        assert [card.flipped for card in game.board.cards if card.word == game.guess][0] is True
        assert game.guess_value == 4
        assert game.code_number == 0


class TestCheckWin:
    '''Check_win is responsible for assigning a winner if the death card 
    is picked or if the entire deck has been flipped'''
    def test_red_wins_if_blue_draws_death(self):
        'test if winner_color is the opposite team and game_over is True'
        game = Game()
        game.guess_value = 4
        game.team = "blue"

        game.check_win()

        assert game.winner_color == 'red'
        assert game.game_over is True

    def test_blue_wins_if_red_draws_death(self):
        'test if when team is "red", winner_color is "blue"'
        game = Game()
        game.guess_value = 4
        game.team = "red"

        game.check_win()

        assert game.winner_color == 'blue'
        assert game.game_over is True

    def test_red_complete_deck(self):
        'test if when all red cards are flipped, winner_color = red and game_over is True'
        game = Game()
        # make all red cards guessed
        for card in game.board.cards:
            if card.color == 'red':
                card.flipped = True

        game.check_win()

        assert game.winner_color == 'red'
        assert game.game_over is True

    def test_blue_complete_deck(self):
        'test if when all blue cards are flipped, winner_color = blue and game_over is True'
        game = Game()
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
        'If our last guess was correct and we have guesses left and the game is not over, we should get another guess'
        game = Game()
        game.guess_value = 1
        game.code_number = 1
        game.game_over = False

        game.update_state()

        assert game.guessing is True

    def test_game_over_and_skip_are_true_makes_guessing_false(self):
        'When game_over is True guessing is False. When skip is True, it is changed to False'
        'Team color is changed from blue to red. Guess_value is reset'
        game = Game()
        game.guess_value = 1
        game.code_number = 1
        game.game_over = True
        game.skip = False

        game.update_state()

        assert game.skip is True
        assert game.guessing is True

    def test_guessing_is_false_when_code_number_is_zero(self):
        'If code_number is 0, guessing should be False'
        'Team color is changed from red to blue. Guess_value is reset'
        game = Game()
        game.guess_value = 1
        game.code_number = 0
        game.game_over = False
        # need skip to be True so that self.guessing is not reset to True before test
        game.skip = True
        game.team = "red"

        game.update_state()

        assert game.skip is False
        assert game.guessing is False
        assert game.team == "blue" # team color should be switched if game.skip is False
        assert game.guess_value == 0 # guess_value should reset if game.skip is False

    def test_guessing_is_false_when_guess_value_is_greater_than_one(self):
        'If guess_value is more than one, guessing should be False'
        game = Game()
        game.guess_value = 2
        game.code_number = 1
        game.game_over = False
        # need skip to be True so that self.guessing is not reset to True before test
        game.skip = True

        game.update_state()

        assert game.skip is False
        assert game.guessing is False

    def test_skip_is_true_when_first_guessing_is_false(self):
        'When guessing is false and skip is false, skip and guessing should be changed to True'
        game = Game()
        game.skip = False
        
        assert game.guessing is False

        game.update_state()

        assert game.skip is True
        assert game.guessing is True
