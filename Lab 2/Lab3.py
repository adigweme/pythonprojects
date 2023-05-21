#******************************************************************************
# Author:           Patrick Adigweme
# Lab:              Lab 3
# Date:             2023-04-22
# Description:      This program calculates net income.
# Input:            This program takes (float) gross income and (float) taxes
#                   as input.
# Output:           This program outputs (float) net income to the console.
# Sources:          Lab 2 & 3 specifications
#******************************************************************************

# What is your gross income for the time period? $100000
# What is your estimated effective tax rate? 25
# Your net income for the time period is: $75000


def main():
    """
    Calculate user's net income based on user input of gross income and
    tax rate.
    :return: Output a string containing a float with result of calculations.
    """
    output_greeting()
    gross_income = input_gross_income()
    tax_rate = input_tax_rate()
    tax_rate_percentage = calculate_tax(tax_rate)
    net_income = calculate_net_income(gross_income, tax_rate_percentage)
    output_results(net_income)


def output_greeting():
    """
    Greet the user of this program.
    :return: A welcome message.
    """
    print("Welcome to the Net Income Calculator!\n")


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
