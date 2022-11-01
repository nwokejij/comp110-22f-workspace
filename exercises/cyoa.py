"""Choose your own adventure."""
__author__ = "730555056"
import random
points: int = 1
player: str = ""
response: str = ""
HAPPY_EMOJI: str = "\U0001F603"
SAD_EMOJI: str = "\U0001F62D"
REALLY_EMOJI: str = "\U0001F611"
TONGUE_OUT: str = "\U0001F61D"
DEVIL: str = "\U0001F608"
MAD_EMOJI: str = "\U0001f620"


def greet() -> None:
    """Welcomes the user and asks for user's name."""
    global player 
    player = input("Hello there, what is your name?\n")


def main() -> None:
    """The program."""
    global points 
    global player
    global response
    greet()
    # game loop
    while True:
        valid: bool = False
        response = input(f"Ok {player}, you are about to play a game that will determine whether or not you are lucky or not. \nHowever, the more you play, the less lucky you are, so you best be lucky early on or you will be frustrated very quickly.\nFirst off, I will present you with three choices. Pick the number (1, 2, 3) you want to choose.\n1. I just want to play the game so LET'S JUST GO ALREADY! {HAPPY_EMOJI}\n2. You can't tell me what to do. I'M IN CONTROL OF THIS SITUATION COWBOY.\n3. Forget you man, I'm outta here.\n")
        while not valid:
            # branch 1, 2, and 3
            if response == str(1):
                valid = True
                test1_procedure()
            elif response == str(2):
                valid = True
                print("Total Points: " + str(test2_function(points)))
            elif response == str(3):
                valid = True
                test3_procedure()
            else:
                # makes sure user response is in the right format
                response = input(f"Please enter the correct format, {player} (1, 2, or 3).\n")


def test1_procedure() -> None:
    """User will guess a number between two integers. If user is right, the program ends, but if wrong, user will choose to continue the game or not."""
    global points
    global response
    print(f"Ok then. The purpose of this game is to guess the correct number from a list of random integers in the least amount of points as possible.\nThe lowest possible point is 1. Simple enough right?\nThe catch is that the list of numbers increases by one if you get it wrong.\nTry it {player}!")
    response_int: int 
    end_game: bool = False
    valid: bool = False
    rand_numb: int
    last_number: int = 2
    while not end_game:
        # this loop repeats until game ends
        rand_numb = ran_int(1, last_number)
        response_int = int(input(f"Choose one number from the numbers 1 to {last_number}. Super easy right?\n"))
        while response_int < 1:
            # makes sure user enters correct input
            response_int = int(input(f"{player}, please choose a number between 1 and {last_number}\n"))
        if response_int == rand_numb:
            # user wins game if he/she/they guess the random number correctly
            end_game = True
            print(f"Congratulations {player}, you won this game with {points} points!!!!")
            print(f"{HAPPY_EMOJI} {HAPPY_EMOJI} {HAPPY_EMOJI} {HAPPY_EMOJI}")
        else:
            # user has choice whether to continue or end the game if user guesses incorrectly
            response = input("OH NO! You weren't lucky this time. Maybe you should quit? Reply Y/N\n")
            valid = False
            while not valid:
                if response == "Y":
                    print(f"It's sad to see you go!!! You had {points} points.")
                    print(f"{SAD_EMOJI}{SAD_EMOJI}{SAD_EMOJI}{SAD_EMOJI}{SAD_EMOJI}")
                    valid = True
                    end_game = True
                elif response == "N":
                    points += 1
                    valid = True
                    print(f"I applaud your tenacity. Let's try this again. You currently have {points} points. But remember, this time the number of integers increase by 1!!! Good luck!")
                    last_number += 1
                else:
                    # makes sure response is valid
                    response = input("Please answer with either Y or N.\n")


def test2_function(score: int) -> int:
    """User chooses the two numbers that the random number should be between. If user is right, user wins, but if user is wrong, the last number increases by 1 like before."""
    global player
    # User chooses the first and last number of range
    user_first: int = int(input(f"Ok since you want to have things your way, {player} {REALLY_EMOJI}. Choose whatever number greater than one that you want to start with, you brat! {TONGUE_OUT}\n"))
    # makes sure user_first has right conditions
    while user_first <= 1:
        user_first = int(input(f"Please follow directions, {player}. Input a number greather than 1 {MAD_EMOJI}\n"))
    user_last: int = int(input(f"OK, {player} now choose which number you want to be the last number. Remember it MUST be greater than the first number you just entered.\n"))
    # makes sure user_last has right conditions
    while user_last <= user_first:
        user_last = int(input("Make sure this number is greater than the first number!!!\n"))
    print(f"BUT there's a twist to the tale. NOW, when you guess incorrectly, the difference between the random answer and your guess is added to your points tally. MUAHHAHHAHAHAH {DEVIL} {DEVIL} ")
    # Round is played, user makes a guess, returns user's points at the end
    return mini2_function(score, user_first, user_last)


def mini2_function(new_score: int, first: int, last: int) -> int:
    """Will run the game with the first number and the last number that the user set."""
    global response
    out_of_bounds: bool
    while True:
        rand_numb2: int = ran_int(first, last)
        response_int2: int = int(input(f"Choose a number from {first} to {last}\n"))
        # makes sure user input fits requirements
        while response_int2 < first or response_int2 > last:
            response_int2 = int(input(f"Please choose a number from {first} to {last}\n"))
            # If user makes a correct guess, the amount of points is returned, if user gives up, amount of points is returned.
        if response_int2 == rand_numb2:
            print(f"Congratulations {player}, you won this game!!!!")
            print(f"{HAPPY_EMOJI} {HAPPY_EMOJI} {HAPPY_EMOJI} {HAPPY_EMOJI}")
            return new_score
        else:
            # The difference between guess and correct answer is added to points
            new_score += abs(response_int2 - rand_numb2)
            response = input("OH NO! You weren't lucky this time. Maybe you should quit? It might be getting to hard for you. Reply Y/N\n")
            out_of_bounds = True
            while out_of_bounds:
                if response == "Y":
                    out_of_bounds = False
                    print(f"It's sad to see you go, {player}!!!")
                    print(f"{SAD_EMOJI}{SAD_EMOJI}{SAD_EMOJI}{SAD_EMOJI}{SAD_EMOJI}")
                    return new_score
                elif response == "N":
                    out_of_bounds = False
                    print(f"I applaud your tenacity. Let's try this again. You currently have {new_score} points. But remember, this time the number of integers increase by 1!!! Good luck!")
                    last += 1
                else:
                    # makes sure user response is either Y or N
                    response = input(f"Come on, {player}. Follow the instructions. Enter Y or N.\n")


def test3_procedure() -> None:
    """User gives up. Boo user."""
    print(f"Ok, {player}. I guess you're no fun!!! But you still have {points} points. Goodbye!!")


def ran_int(first: int, last: int) -> int:
    """Will return a random int from first to last inclusive."""
    return random.randint(first, last)
    

if __name__ == "__main__":
    main()