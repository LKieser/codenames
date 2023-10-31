"""Main runs the game through a game loop based on the current state: Codegiver turn or Decoder turn.
The game loop begins with render then process input then update state. This repeats until the end conditions are met."""
from game import Game


def main():
    """Initial lines are used to begin the game and will only run once.
    Loop will continue till end of game conditions are met."""
    # Initial game.
    game = Game()

    # Initial board.
    game.render(guessing = True)
    input('\nPress "Enter" when you are ready to begin the game: ')

    while True:
        game.render()

        # Process input.
        if game.game_over:
            break
        
        if not game.skip:
            if game.guessing:
                game.take_guess()
            else:
                game.create_code_word()

            # Update state
            if game.guessing:
                game.check_guess()
                game.check_win()
        game.update_state()

if __name__ == "__main__":
    main()
