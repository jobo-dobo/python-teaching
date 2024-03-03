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
        input_option = input("Do you want to quit? (y/n) ")
        if input_option.lower().strip() in {"y", "yes", "yeah", "yee"}:
            is_running = False




if __name__ == "__main__":
    hangman_game()
