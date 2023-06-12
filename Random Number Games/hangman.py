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
import dictionaries as d


class Board:
    __length = 0
    __layout = ""

    def __init__(self, length):
        self.__length = length

    def __str__(self):
        return self.__layout

    def get_layout(self):
        return self.__layout

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def initialize_board(self):
        self.__layout = "_" * self.__length
        print(self.__layout)

    def update_board(self, guess, spot):
        word_as_list = list(self.__layout)
        word_as_list[spot] = guess
        self.__layout = "".join(word_as_list)


def main():
    """
    A simple game of hangman using a list from the dictionaries module.
    :return:
    """
    game_dict = []
    word = ""
    word_as_list = []
    guesses = []
    chosen_dict = 0
    word_selector = 0
    guess = ""
    correct = ""
    spot = 0
    tries = 0
    state = 0

    chosen_dict = choose_game()
    game_dict = set_dictionary(chosen_dict)
    word_selector = r.randint(0, len(game_dict))
    word = get_word(word_selector, game_dict)
    word_as_list = list(word)
    play_board = Board(len(word))
    play_board.initialize_board()
    while state == 0:
        guess = input_guess(guesses)
        guesses.append(guess)
        correct = determine_guess(guess, word)
        output_guess_again(guess, correct)
        if correct is True:
            for i in range(len(word_as_list)):
                if word_as_list[i] == guess:
                    play_board.update_board(guess, i)
        print("\n", play_board.__str__())
        tries = tries + 1
        if play_board.get_layout() == word:
            output_congrats(tries)
            state = 1


def get_word(word_selector, game_dict):
    """
    Get the word corresponding to randomized choice.
    :return: string containing word for user to guess
    """
    word = ""

    word = game_dict[word_selector]
    word = word.lower()
    return word


def choose_game():
    """
    Allow use to choose the dictionary the program will pick words from.
    :return: numerical value corresponding to dictionary
    """
    game = 0

    print("Available game options are:\n1. U.S. States\n2. Fruits\n3. Uncommon Words")
    while True:
        game = v.get_integer("Please choose a number from the available options.\n")
        if 0 < game < 4:
            return game
        else:
            print("Please enter a valid selection.")


def set_dictionary(chosen_dict):
    """
    Set the dictionary for the game to user selection.
    :return: dictionary to use in subsequent functions
    """

    if chosen_dict == 1:
        return d.dict_0_state
    elif chosen_dict == 2:
        return d.dict_1_fruit
    elif chosen_dict == 3:
        return d.dict_2_words


def input_guess(guesses):
    """
    Prompt for and return a character
    :return: user inputted character
    """
    guess = ""

    while True:
        guess = v.guess_letter()
        if guess not in guesses:
            return guess
        else:
            print(f"You have already guessed {guess}!")


def determine_guess(guess, word):
    """
    Determine if user guess is in word.
    :param guess: user inputted character guess
    :param word: secret word, a string
    :return: correctness of guess as true/false
    """

    if guess in word:
        return True
    else:
        return False


def output_guess_again(guess, state):
    """
    Instruct user to guess again if incorrect letter was guessed
    :param guess: user inputted character of guess
    :param state: determined true/false by prior function if guess correct or not
    :return:
    """
    if state is True:
        print(f"\nYou guessed {guess}, which is in the secret word!")
    elif state is False:
        print(f"\nYou guessed {guess}, which is not in the secret word.")


def output_congrats(tries):
    """
    Congratulation message with number of tries.
    :param tries: int, number of tries to guess the secret word
    :return:
    """
    print(f"Congratulations! You found the secret word in only {tries} tries.")


main()
