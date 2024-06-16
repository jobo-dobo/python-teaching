from random import randrange
import click

from hangman_constants import HANGMANPICS, HANGMANWORDS

NUM_WRONG_GUESSES = len(HANGMANPICS) - 1


def hangman_game():
    is_running = True
    is_new_game = True
    goal_word = None
    guessed_letters = set()

    # program/game loop
    while is_running:
        # clear console
        click.clear()
        # initialize new game
        if is_new_game:
            print("Welcome to my hang, man")
            # pick a random word
            goal_word = HANGMANWORDS[randrange(len(HANGMANWORDS))]
            # print(goal_word)
            # reset is_new_game and guesses
            is_new_game = False
            guessed_letters = set()

        # show game state (hangman, guesses, word)
        render_game_state(goal_word, guessed_letters)

        # check for end state
        is_end_game = False
        # win!
        correct_letters = set(goal_word) & guessed_letters
        if len(set(goal_word)) == len(correct_letters):
            print("YOU WIN!!!!!")
            is_end_game = True
        # lose
        elif len(guessed_letters - correct_letters) == NUM_WRONG_GUESSES:
            print("You LOST, sad! x_x")
            print(f'The correct word was "{goal_word}"')
            is_end_game = True

        # end of game, quit or continue with new game?
        if is_end_game:
            input_option = input("Do you want to quit? (y/n) ")
            if input_option.lower().strip() in {"y", "yes", "yeah", "yee"}:
                is_running = False
            else:
                is_new_game = True
            continue

        # give player a guess
        input_letter = input("Guess a letter :3 : ")
        valid_letter = validate_input_letter(input_letter)

        # do nothing if invalid input
        if valid_letter is None:
            continue
        # add valid letter to guesses
        guessed_letters.add(valid_letter)
        # correct
        if valid_letter and valid_letter in goal_word:
            print("Success")
        elif valid_letter:
            print("NO WRONG")


def render_game_state(goal_word, guessed_letters):
    # word state - has _ for non-guessed letters,
    # and shows letters correctly guessed in their
    # place; e.g. for "moderate" with {"d", "e", "f"}
    # guessed, shows "_ _ d e _ _ _ e"
    word_state = " ".join(
        [letter if letter in guessed_letters else "_" for letter in goal_word]
    )
    wrong_letter_set = guessed_letters - set(goal_word)
    wrong_letter_string = " ".join(sorted(wrong_letter_set))
    hangman_pic = HANGMANPICS[len(wrong_letter_set)]
    # print guesses, hangman, and word state
    print("Incorrect guesses: " + wrong_letter_string)
    print(hangman_pic)
    print(word_state)


# later we will throw an exception instead of returning None!
def validate_input_letter(input_letter):
    if len(input_letter) > 1:
        print(f'"{input_letter}" is longer than one letter!')
        return None
    if not input_letter.isalpha():
        print(f'"{input_letter}" is not a valid letter (a-z)!')
        return None
    return input_letter.lower()


if __name__ == "__main__":
    hangman_game()
