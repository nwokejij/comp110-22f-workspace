"""EX02- One shot Wordle."""
__author__ = "730555056"
word: str = "python"
word_length: int = len(word)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
j: int = 0
colors: str = ""
guess: str = input("What is your " + str(word_length) + "-letter guess? ")
 
while len(guess) != word_length:
    guess = input("That was not " + str(word_length) + " letters! Try again: ")
 
 
if len(guess) == word_length:
    while i < len(guess):
        if guess[i] == word[i]:
            colors += GREEN_BOX
        else:
            j = 0
            contained: bool = False
            while j < len(guess):
               
                if guess[i] == word[j]:
                    contained = True
                j += 1
            if contained is True:
                colors += YELLOW_BOX
            else:
                colors += WHITE_BOX
        i += 1
 
    print(colors)
    if guess != word:
        print("Not quite. Play again soon!")
    else:
        print("Woo! You got it!")
