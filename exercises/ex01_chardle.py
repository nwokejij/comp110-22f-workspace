"""EX01- Chardle -A cute step toward Wordle."""
__author__ = "730555056"
counter: int = 0
five_word = input("Enter a 5-character word: ")
if len(five_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
char = input("Enter a single character: ")

if len(char) != 1:
    print("Error: Character must be a single character.")
    exit()

if char == " ":
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + char + " in " + five_word)

if char == five_word[0]:
    print(char + " found at index 0")
    counter = counter + 1

if char == five_word[1]:
    print(char + " found at index 1")
    counter = counter + 1

if char == five_word[2]:
    print(char + " found at index 2")
    counter = counter + 1

if char == five_word[3]:
    print(char + " found at index 3")
    counter = counter + 1

if char == five_word[4]:
    print(char + " found at index 4")
    counter = counter + 1


if counter == 0:
    print("No instances of " + char + " found in " + five_word)
else: 
    if counter == 1:
        print(str(counter) + " instance of " + char + " found in " + five_word)
    else:
        print(str(counter) + " instances of " + char + " found in " + five_word)
