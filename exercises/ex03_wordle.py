"""Full-on Wordle."""
__author__ = "730555056"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
first_guess: str = ""


def contains_char(any_length: str, one_char: str) -> bool:
    """Will return True if 'one_char' is found in 'any_length', False otherwise."""
    assert len(one_char) == 1
    i: int = 0
    while (i < len(any_length)):
        if any_length[i] == one_char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a color-codified string (green, yellow, white) when comparing guess with secret."""
    assert len(guess) == len(secret)
    color: str = ""
    j: int = 0
    while (j < len(secret)):
        if contains_char(secret, guess[j]) is False:
            color += WHITE_BOX 
        else:
            if contains_char(secret[j], guess[j]) is False:
                color += YELLOW_BOX
            else:
                color += GREEN_BOX
        j += 1
    return color


def input_guess(explength: int) -> str:
    """Given an integer, if the length of guess equals explength, the guess will be returned. Otherwise, user will be prompted to input a guess that with the length of explength."""
    first_guess = input(f"Enter a {explength} character word: ")
    while len(first_guess) != explength:
        first_guess = input(f"That wasn't {explength} chars! Try again: ")
    return first_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    correct_length: str = ""
    turn: int = 1
    win: bool = False
    while win is False and turn < 7:
        print(f"=== Turn {turn}/6 ===")
        correct_length = input_guess(len(secret_word))
        print(emojified(correct_length, secret_word))
        if correct_length == secret_word:
            win = True
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
            if turn >= 7:
                print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
