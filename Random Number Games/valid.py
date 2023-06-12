def get_integer(prompt="Please enter an integer: "):
    """
    Function to prompt for and return a valid integer.
    :param prompt: string Optional string to use as prompt
    :return: integer Valid integer
    """
    num = 0
    while True:
        try:
            num = int(input(prompt))
            return num
        except:
            print("Invalid integer.")


def get_real(prompt="Please enter an real number: "):
    """
    Function to prompt for and return a valid real number
    :param prompt: string Optional string to use as prompt
    :return: float Valid real number
    """
    num = 0.0
    while True:
        try:
            num = float(input(prompt))
            return num
        except:
            print("Invalid number.")


def get_hours(prompt="Please enter a number of hours: "):
    """
    Function to prompt for and return a valid real number
    :param prompt: string Optional string to use as prompt
    :return: float Valid real number
    """
    num = 0.0
    while True:
        try:
            num = float(input(prompt))
            if num < 24.001:
                return num
            else:
                num = num / 0
        except:
            print("Invalid number. You cannot enter more than 24 hours.")


def get_string(prompt="Please enter a string: "):
    """
    Function to prompt for and return a string of characters.
    An empty string is invalid input.
    :param prompt: string Optional string to use as prompt
    :return: string Non-empty string of characters
    """
    chars = ""
    while True:
        chars = input(prompt)
        if chars != "":
            return chars
        else:
            print("Invalid string.")


def get_day(prompt="Please enter a string: "):
    """
    Function to prompt for and return a day of the week.
    Any string not in the list is invalid input
    :param prompt: string Optional string to use as prompt
    :return: string Non-empty string of characters
    """
    chars = ""
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    while True:
        chars = input(prompt)
        chars = chars.upper()
        if chars != "" and chars in days:
            return chars
        else:
            print("Invalid selection. Please enter a day of the week. (ex. Tuesday)")


def get_y_or_n(prompt="Please enter 'Yes' or 'No': "):
    """
    Function to prompt for and return 'y' or 'n'.
    'Y', 'N', and all cases of 'yes' and 'no' are accepted.
    :param prompt: string Optional string to use as prompt
    :return: string Non-empty string of characters
    """
    answer = ""
    answer = input(prompt)
    answer = answer.lower()

    while answer != "n" and answer != "y" and answer != "no" and answer != "yes":
        print("Invalid response.")
        answer = input(prompt)
        answer = answer.lower()

    return answer[0]


def get_date(prompt="Please enter a date: "):
    """
    Function to prompt for and return a valid date.
    :param prompt: string Optional string to use as prompt
    :return: integer Valid integer
    """
    num = ""
    thirty_days = ["SEPTEMBER", "APRIL", "JUNE", "NOVEMBER"]
    thirty_one_days = ["JANUARY", "MARCH", "MAY", "JULY", "AUGUST", "OCTOBER", "DECEMBER"]
    twenty_eight_days = "FEBRUARY"

    while True:
        try:
            num = input(prompt)
            num, num0 = num.split(" ")
            num0 = int(num0)
            num = num.upper()

            if num != "" and (num in thirty_days) and 0 < num0 < 31:
                num = num + " " + str(num0)
                return num
            elif num != "" and (num in thirty_one_days) and 0 < num0 < 32:
                num = num + " " + str(num0)
                return num
            elif num != "" and (num == twenty_eight_days) and 0 < num0 < 29:
                num = num + " " + str(num0)
                return num
            else:
                print("Invalid date selection. Please enter a month and day. (ex. May 23)")
        except:
            print("Invalid date selection. Please enter a month and day. (ex. May 23)")


def get_int_below_1000(prompt="Please enter a number: "):
    """
    Function to prompt for and return a valid integer.
    :param prompt: string Optional string to use as prompt
    :return: integer Valid integer
    """
    num = 0
    while True:
        try:
            num = int(input(prompt))
            if 0 < num < 1001:
                return num
            else:
                print("Invalid guess. Please enter a number between 1 and 1000.")
        except:
            print("Invalid guess. Please enter a number between 1 and 1000.")


def guess_letter(prompt="Please enter a letter: "):
    """
    Function ot prompt for an return a letter.
    :param prompt: string Optional string to use as prompt
    :return: single character as a string
    """
    while True:
        try:
            letter = input(prompt)
            if letter.isalpha() and 0 < len(letter) < 2:
                return letter.lower()
            else:
                print("Invalid guess. Please enter a letter of the alphabet.")
        except:
            print("Invalid guess. Please enter a letter of the alphabet.")
