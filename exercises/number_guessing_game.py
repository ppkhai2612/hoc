"""Build a program to create a number guessing game.

Requirements:
1. The program will automatically generate a random number between 1 and 100.
2. Prompt the player to input a number for their guess.
3. Display a message if the guessed number is higher or lower than the random number and indicate the remaining guess count.
4. When the player correctly guesses the number, display the number of guesses needed and notify them that they guessed correctly.
5. After each guessing round, ask the player if they want to play again. If yes, generate a new random number and restart the game."""

import random # import module


def prompt():
    range_of_numbers = [i for i in range(min_number, max_number + 1)] # Generate 1 list include integers from 1-100

    while True:
        guess = input("Enter your guess: ")
        if len(guess) == 0 or not guess.isdecimal() or int(guess) not in range_of_numbers: # Check for invalid player inputs
            print("Guess must be an integer from 1-100")
            continue
        guess = int(guess)
        break
    return guess

def round_of_game(secret_number, guess):
    global guess_count, min_number, max_number
    guessed_numbers = [] # List of numbers that players have guessed

    while guess_count <= guess_limit:
        remaining_guesses = guess_limit - guess_count # used to keep track of the number of guesses remaining
        current_number = guess # Used to update the minimum and maximum values

        if guess in guessed_numbers:
            print("This number has been guessed.")
            guess = prompt()
            continue

        if guess > secret_number:
            if guess_count == guess_limit:
                print(f"You lose. The secret number is {secret_number}.")
                break

            guessed_numbers.append(guess)
            max_number = current_number
            print(f"Your number is higher than the number I picked. It ranges between {min_number} and {current_number}.")
            print(f"You only have {remaining_guesses} guesses left")
            guess = prompt()

        elif guess < secret_number:
            if guess_count == guess_limit:
                print(f"You lose. The secret number is {secret_number}.")
                break

            guessed_numbers.append(guess)
            min_number = current_number
            print(f"Your number is lower than the one I picked. It ranges between {current_number} and {max_number}.")
            print(f"You only have {remaining_guesses} guesses left")
            guess = prompt()

        else:
            print(f"Correct! You guessed the number {secret_number} in {guess_count} tries.")
            break

        guess_count += 1

def play_again():
    again = input("Do you want to play again ? (Yes/No): ")
    if again.lower().startswith("n"):
        print("Thanks for playing.")
    elif again.lower().startswith("y"):
        play()
    else:
        print("Only enter 'y' or 'n'")
        play_again()

def play():
    # Welcome message
    print("Welcome to the Number Guessing Game! \n\nI have selected a random number between 1 and 100. \nTry to guess what it is!\n")

    # Update global variables when the player wants to play again
    """Guess_limit: Maximum number of times a player can guess
    Guess_count: loop variable"""
    global min_number, max_number, guess_limit, guess_count
    min_number, max_number = 1, 100
    guess_limit, guess_count = 5, 1

    # Generate a random number between 1-100
    secret_number = random.randint(min_number, max_number)

    # Prompt the user input
    guess = prompt()

    # Round of game
    round_of_game(secret_number, guess)

    # Play again
    play_again()


play()