#******************************************************************************
# Author:           Patrick Adigweme
# Lab:              Lab 9
# Date:             2023-06-03
# Description:      This program calculates net income.
# Input:            This program takes various float and string inputs.
# Output:           This program outputs net income and hourly rate, if hours
#                   are entered by the user.
# Sources:          Lab 2 & 3 & 4 & 5 & 6 & 7 & 9 specifications
#******************************************************************************

# Welcome to N.I.C.E., the Net Income Calculator Experience!
#
# What is your hourly rate of pay?
# $48.08
# What is your estimated effective tax rate?
# Enter the percentage as a whole number (e.g. 25 for 25%)
# 25
# How many hours will you work in this period?
# 49
# Do you want to break that out by day?
# Yes
# How many days?
# 5
# What was the date of day 1? May 22
# What day of the week was day 1? Monday
# How many hours did you work that day? 10
#
# What was the date of day 2? May 23
# What day of the week was day 2? Tuesday
# How many hours did you work that day? 10
#
# What was the date of day 3? May 24
# What day of the week was day 3? Wednesday
# How many hours did you work that day? 10
#
# What was the date of day 4? May 25
# What day of the week was day 4? Thursday
# How many hours did you work that day? 10
#
# What was the date of day 5? May 26
# What day of the week was day 5? Friday
# How many hours did you work that day? 9
#
# Your total gross income based on your hours worked is $2355.92.
# Based on your gross income and your effective tax rate,
# your net income for the time period should be: $1766.94
# Would you like to see this broken out by day? Yes
#
# Here you go:
# Date                Day            Net Pay
# ________________    ________________ ________________
# May 22              MONDAY         360.60
# May 23              TUESDAY        360.60
# May 23              WEDNESDAY      360.60
# May 24              THURSDAY       360.60
# May 25              FRIDAY         324.54
#
# Would you like to perform another calculation? (Yes/No) No
# Have a N.I.C.E. day!


import valid
import list


class Shifts:
    __date = ""
    __day = ""
    __hours = 0.0

    def __init__(self, date, day, hours):
        self.__date = date
        self.__day = day
        self.__hours = hours

    def __str__(self):
        return f"Shift on {self.__date}, a {self.__day}, for {self.__hours}" \
               f" hours."

    def get_date(self):
        return self.__date

    def get_day(self):
        return self.__day

    def get_hours(self):
        return self.__hours

    def set_date(self, date):
        self.__date = date

    def set_day(self, day):
        self.__day = day

    def set_hours(self, hours):
        self.__hours = hours


def main():
    """
    Calculate user's net income based on user input of gross income and
    tax rate.
    :return: Output a string containing a float with result of calculations.
    """
    hours_worked = 0.0
    hourly_rate = 0.0
    tax_rate = 0.0
    tax_rate_percentage = 0.0
    net_income = 0.0
    hours_redo = 0.0
    hours_by_day = ""
    total_income = 0.0
    state = 0
    shift_list = []
    days_worked = []
    day_worked = ""
    hours_per_day = []
    hour_per_day = 0.0
    days_of_week = []
    day_of_week = ""

    output_greeting()

    while state == 0:
        hourly_rate = input_hourly_rate()
        tax_rate = input_tax_rate()
        tax_rate_percentage = calculate_tax(tax_rate)
        hours_worked = input_number_hours()
        hours_by_day = input_breakdown()
        shift_list = list_builder(hours_by_day)
        total_income = calculate_total(hours_worked, hourly_rate)
        net_income = calculate_net_income(hourly_rate,
                                          total_income, tax_rate_percentage)
        output_results(net_income, total_income, tax_rate)
        more_details = input_further_details()
        if more_details == 'y' and hours_by_day != 'n':
            net_pay = net_per_day(shift_list, net_income)
            output_detail_results(net_pay, shift_list)
        elif more_details == 'y' and hours_by_day == 'n':
            output_no_hourly()
        state = calculate_again()

# ***************** Inputs Functions ***********************


def input_number_hours():
    """
    This function asks the user for a float of hours worked.
    :return: float of hours worked, passed to other functions in the program
    """
    hours_worked = 0.0
    hours_worked = valid.get_real("How many hours will you work in this "
                                  "period? \n")
    return hours_worked


def input_hourly_rate():
    """
    Take user input to define initial variables for calculation
    :return: float value for gross income to the main function
    """
    hourly_rate = 0.0
    hourly_rate = valid.get_real("What is your hourly rate of pay?\n$")
    return hourly_rate


def input_tax_rate():
    """
    Take user input to define initial variable for calculation
    :return: float value for tax rate to the main function
    """
    tax_rate = 0.0
    tax_rate = valid.get_int_below_100("\nWhat is your estimated effective"
                                       " tax rate?\nEnter the percentage as "
                                       "a whole number (e.g. 25 for 25%)\n")
    return tax_rate


def input_further_details():
    """
    Prompt user for further details.
    :return: user choice as y/n
    """
    details = ""
    details = valid.get_y_or_n("Would you like to see this broken out "
                               "by day? (y or n)\n")
    return details
# ***************** Calculation / Selection Functions ***************


def calculate_tax(tax_rate):
    """
    Calculate the tax rate as a percentage
    :param tax_rate: a float passed from a prior function
    :return: a float less than 1
    """
    tax_rate_percentage = 0.0
    tax_rate_percentage = tax_rate / 100
    return tax_rate_percentage


def calculate_net_income(hourly_rate, total_income, tax_rate_percentage):
    """
    Calculate the user's net income
    :param total_income: calculated total income as float
    :param hourly_rate: a float passed from a prior function
    :param tax_rate_percentage: a float passed from a prior function
    :return: User's net income as a float
    """
    net_hourly_rate = 0.0
    net_income = 0.0

    net_hourly_rate = hourly_rate * (1 - tax_rate_percentage)
    net_income = total_income * (1 - tax_rate_percentage)
    return net_hourly_rate, net_income


def calculate_total(hours_worked, hourly_rate):
    """
    This function calculates the hourly wage for the user.
    :param hourly_rate: user inputted float from prior function
    :param hours_worked: user inputted float from prior function
    :return: float, calculation of hourly wage from two params
    """
    total = 0.0

    if hours_worked != 0:
        total = hourly_rate * hours_worked
    elif hours_worked == 0:
        output_no_hourly()
    return total


def calculate_again():
    state = 0
    choice = ""
    choice = valid.get_y_or_n("\n\nWould you like to perform"
                              " another calculation? (Yes/No) \n")
    if choice == "y":
        state = 0
        print("\n\n")
        return state
    elif choice == "n":
        state = 1
        print("Have a N.I.C.E. day!")
        return state


def input_breakdown():
    """
    this function lets the user enumerate hours by day
    :return:
    """
    by_day = ""
    num_of_days = 0

    by_day = valid.get_y_or_n("Would you like to break that out by day?"
                              " (Yes/No) \n")
    if by_day == 'y':
        num_of_days = valid.get_integer("How many days? \n")
        return by_day, num_of_days
    else:
        return by_day


def net_per_day(shift_list, net_income):
    """
    Calculate net pay per hours worked per day.
    :param net_income: list containing calculated net values
    :param shift_list: list of Shifts objects
    :return:
    """
    net_pay = []
    for i in range(len(shift_list)):
        net = shift_list[i].get_hours() * net_income[0]
        net_pay.append(net)
    return net_pay


def list_builder(hours_by_day):
    """
    Build lists from user inputs
    :param hours_by_day: takes user decision to proceed to build lists.
    :return: three lists as inputted by user
    """
    hour_per_day = 0.0
    day_worked = ""
    day_of_week = ""
    shift_list = []

    if hours_by_day[0] == 'y':
        for i in range(hours_by_day[1]):
            day_worked = valid.get_date(f"\nWhat was the date of day"
                                        f" {i + 1}? (ex. September 2) ")
            day_of_week = valid.get_day(f"What day of the week"
                                        f" was day {i + 1}? ")
            hour_per_day = valid.get_hours("How many hours did you work"
                                           " that day? ")
            shift_list.append(Shifts(day_worked, day_of_week, hour_per_day))

        return shift_list
# ***************** Output Functions ***********************


def output_greeting():
    """
    Greet the user of this program.
    :return: A welcome message.
    """
    print("Welcome to N.I.C.E., the Net Income Calculator Experience!\n")


def output_hourly(hourly_rate):
    """
    This function takes a variable passed from a previous function
    and outputs to the console if that variable is not equal to
    zero.
    :param hourly_rate: a float passed from a previous function
    :return: print the hourly rate to the console
    """
    if hourly_rate != 0:
        print(f"\nYour total salary is ${hourly_rate:.2f}.")
    else:
        return


def output_no_hourly():
    """
    this function prints to the console if the user doesn't
    specify an hourly rate.
    :return: Print a message to the console.
    """
    print("\nSorry, you did not input any days. A daily "
          "breakdown cannot be generated.")


def output_results(net_income, total_income, tax_rate):
    """
    Output final calculation results ot the user
    :param total_income: calculated total from list, float
    :param net_income: a float passed from a prior function
    :param tax_rate: a user defined int for tax percentage
    :return: Print a message including user's net income to console.
    """
    print(f"\nYour total gross income based on your hours worked"
          f" is ${total_income:.2f}.")
    print(f"Based on your gross income and your effective "
          f"tax rate of {tax_rate:.0f}%, your net income for the time period"
          f" should be ${net_income[1]:.2f}.")
    print(f"That equates to a net hourly rate of ${net_income[0]:.2f}.")


def output_detail_results(net_pay, shift_list):
    """
    Output calculations as a table against all entered data
    :param shift_list: list of all Shifts objects
    :param net_pay: list of net pay for all hours per day
    :return: print a message to the console.
    """
    print("\nHere you go:")
    print("{: <20}{: <20}{: <20}".format("Date", "Day", "Net Pay"))
    print("{: <20}{: <20}{: <20}".format("______________ ",
                                         "______________ ",
                                         "______________"))

    for i in range(len(shift_list)):
        print("{: <20}{: <20}{: <20}".format(shift_list[i].get_day(),
                                             shift_list[i].get_date(),
                                             f"${net_pay[i]:.2f}"))

# ***************** Run Main Function ***********************


main()
