import random

number = random.randint(1, 1000)
player_name = input("Hi! What's your name? ")
number_of_guesses = 0
print(
    "Great! "
    + player_name
    + ", I am going to pick a number between 1 and 1000, try guessing it. Good luck!"
)

while number_of_guesses < 15:
    guess = int(input())
    number_of_guesses += 1

    if guess < number:
        print("Your number is too low.")
    elif guess > number:
        print("Your number is too high.")
    else:
        break

if guess == number:
    print(
        "Congratulations, "
        + player_name
        + "! You guessed the number in "
        + str(number_of_guesses)
        + " tries!"
    )
else:
    print(
        "Sorry, "
        + player_name
        + ", you did not guess the number. The number was "
        + str(number)
        + "."
    )
