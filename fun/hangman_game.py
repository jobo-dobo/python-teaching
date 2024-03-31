from random import randrange
import click

from hangman_constants import HANGMANPICS, HANGMANWORDS

mydict = {
    "a": "aaaaaa",
    "b": "bbbuuuuh",
    "c": "c",
}

def hangman_game():
    is_running = True
    while is_running:
        print("Welcome to my hang, man")
        # pick a random word
        goal_word = HANGMANWORDS[randrange(len(HANGMANWORDS))]
        print(goal_word)

        # give player a guess
        input_letter = input("Guess a letter :3 : ")
        valid_letter = validate_input_letter(input_letter)
        
        # guess result
        if valid_letter and valid_letter in goal_word:
            print("Success")
        else:
            print("NO WRONG")

        # quit thing
        input_option = input("Do you want to quit? (y/n) ")
        if input_option.lower().strip() in {"y", "yes", "yeah", "yee"}:
            is_running = False


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
