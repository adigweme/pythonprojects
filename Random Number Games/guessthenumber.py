# *************************************************************************************
#
# Created by: Patrick Adigweme
# Date: June 11, 2023
#
#
#
#
# *************************************************************************************

import random as r
import valid as v


def main():
    """
    This program is a random number guessing game created for practice and
    simple enjoyment.
    :return:
    """
    ready_to_play = ""
    secret_number = r.randint(0, 1000)
    guessed = "n"
    guess = 0
    number_guessed = 0
    tries = 0
    again = ''

    output_greeting()
    ready_to_play = input_start()
    if ready_to_play == 'y':
        while guessed == "n":
            guess = input_guess()
            if guess == secret_number:
                tries = tries + 1
                output_correct(guess, tries)
                again = v.get_y_or_n("\nWould you like to play again?\n")
                if again == 'y':
                    guessed = "n"
                    secret_number = r.randint(0, 1000)
                elif again == 'n':
                    guessed = "y"
            elif guess > secret_number:
                delta = calculate_delta(guess, secret_number)
                output_distance(guess, delta)
                tries = tries + 1
            elif secret_number > guess:
                delta = calculate_delta(guess, secret_number)
                output_distance(guess, delta)
                tries = tries + 1
        output_goodbye()
    elif ready_to_play == 'n':
        output_not_starting()

# ************************** Input Functions **********************


def input_start():
    """
    This function determines if the game should start
    :return: Y or N, determined by user input
    """
    start_game = ""

    start_game = v.get_y_or_n("Are you ready to begin? (Yes / No)\n")
    return start_game


def input_guess():
    """
    This function takes user input as an int to guess the secret number
    :return: Int between 1 and 100 determined by user
    """
    guess = 0

    guess = v.get_int_below_1000("Please guess a number between 1 and 1000.\n")
    return guess


def calculate_delta(guess, secret_number):
    """
    Calculate delta between guess and secret number
    :param guess: int entered by user
    :param secret_number: randomly generated number
    :return:
    """
    delta = 0

    delta = guess - secret_number
    delta = 1000 - delta
    delta = delta / 10
    return delta

# ***************** Output Functions *************************8


def output_greeting():
    """
    Output initial greeting.
    """

    print("Welcome to the R.N.G., a random number game!")
    print("The program will generate a number between 1 and 1000 and"
          " you'll guess it! Isn't that fun?")


def output_distance(guess, delta):
    """
    Output the distance form guess to secret number.
    :return: output an int to the console passed from prior function
    """

    print(f"You guessed, {guess}, which is {delta}% accurate.")


def output_not_starting():
    """
    Output a message to the console when user chooses not to start game
    :return:
    """

    print("It looks like you're not ready to begin. Please restart the program"
          " when ready.")


def output_correct(guess, tries):
    """
    Congratulation message to the user for a correct guess.
    :return:
    """
    print(f"You guessed {guess}, which is the secret number!")
    print("Congratulations! It took", tries, "tries.")


def output_goodbye():
    """
    This function outputs a goodbye message
    :return:
    """
    print("Thanks for playing!")


main()
