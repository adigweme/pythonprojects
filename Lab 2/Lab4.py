#******************************************************************************
# Author:           Patrick Adigweme
# Lab:              Lab 4
# Date:             2023-04-24
# Description:      This program calculates net income.
# Input:            This program takes (float) gross income and (float) taxes
#                   as input.
# Output:           This program outputs (float) net income to the console.
# Sources:          Lab 2 & 3 & 4 specifications
#******************************************************************************

# What is your gross income for the time period? $100000
# What is your estimated effective tax rate? 25
# How many hours will you work in this period? 2080
# Your net hourly rate is $48.08
# Your net income for the time period is: $75000


def main():
    """
    Calculate user's net income based on user input of gross income and
    tax rate.
    :return: Output a string containing a float with result of calculations.
    """
    hours_worked = 0.0
    gross_income = 0.0
    tax_rate = 0.0
    tax_rate_percentage = 0.0
    net_income = 0.0

    output_greeting()
    gross_income = input_gross_income()
    tax_rate = input_tax_rate()
    tax_rate_percentage = calculate_tax(tax_rate)
    hours_worked = input_number_hours()
    hours_worked = (hours_worked, gross_income)
    calculate_hourly(hours_worked, gross_income)
    net_income = calculate_net_income(gross_income, tax_rate_percentage)
    output_results(net_income)

# Inputs


def input_number_hours():
    """
    This function asks the user for a float of hours worked.
    :return: float of hours worked, passed to other functions in the program
    """
    hours_worked = 0.0
    hours_worked = float(input("How many hours will you work in this period? "))
    return hours_worked


def input_gross_income():
    """
    Take user input to define initial variables for calculation
    :return: float value for gross income to the main function
    """
    gross_income = 0.0
    gross_income = float(input("What is your gross income for the time "
                               "period? \nS"))
    return gross_income


def input_tax_rate():
    """
    Take user input to define initial variable for calculation
    :return: float value for tax rate to the main function
    """
    tax_rate = 0.0
    tax_rate = float(input("\nWhat is your estimated effective tax rate?\n"
                           "Enter the percentage as a whole number (e.g. "
                           "25 for 25%)\n"))
    return tax_rate

# Calculations


def calculate_tax(tax_rate):
    """
    Calculate the tax rate as a percentage
    :param tax_rate: a float passed from a prior function
    :return: a float less than 1
    """
    tax_rate_percentage = 0.0
    tax_rate_percentage = tax_rate / 100
    return tax_rate_percentage


def calculate_net_income(gross_income, tax_rate_percentage):
    """
    Calculate the user's net income
    :param gross_income: a float passed from a prior function
    :param tax_rate_percentage: a float passed from a prior function
    :return: User's net income as a float
    """
    net_income = 0.0
    net_income = gross_income * (1-tax_rate_percentage)
    return net_income


def calculate_hourly(hours_worked, gross_income):
    """
    This function calculates the hourly wage for the user.
    :param gross_income: user inputted float from prior function
    :param hours_worked: user inputted float from prior function
    :return: float, calculation of hourly wage from two params
    """
    hourly = gross_income / hours_worked
    print(hourly)
    return hourly


def hours_decision(hours_worked, gross_income):
    """
    This function checks user input to be sure they mean to enter zero
    for the hours_worked parameter. It then performs a calculation
    if the user indicates that is correct or if the value is greater
    than zero. If the user indicates they did not mean to enter zero,
    it runs the number_hours function again.
    :param gross_income: a float passed from a previous function
    :param hours_worked: a float passed from a previous function
    :return: this function either exits with no return or runs other
    functions as a result of user decisions
    """
    if hours_worked == 0:
        print("You entered zero hours for the period. Was that right?")
        yes_or_no = input("Type Yes or No\n")
        if yes_or_no == "Yes" or yes_or_no == "yes":
            return
        elif yes_or_no == "No" or yes_or_no == "no":
            hours_worked = input_number_hours()
            return hours_worked
    elif hours_worked > 0:
        hourly_rate = 0.0
        hourly_rate = calculate_hourly(hours_worked, gross_income)
        output_hourly(hourly_rate)
        return hours_worked

# Outputs


def output_greeting():
    """
    Greet the user of this program.
    :return: A welcome message.
    """
    print("Welcome to the Net Income Calculator!\n")


def output_hourly(hourly_rate):
    """
    This function takes a variable passed from a previous function
    and outputs to the console if that variable is not equal to
    zero.
    :param hourly_rate: a float passed from a previous function
    :return: print the hourly rate to the console
    """
    if hourly_rate != 0:
        print(f"\nYour hourly rate is ${hourly_rate:.2f}.")
    else:
        return


def output_results(net_income):
    """
    Output final calculation results ot the user
    :param net_income: a float passed from a prior function
    :return: Print a message including user's net income to console.
    """
    print(f"\nBased on your gross income and your effective "
          f"tax rate, your net income for the time period"
          f" should be ${net_income:.2f}.")


main()
