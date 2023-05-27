#******************************************************************************
# Author:           Patrick Adigweme
# Lab:              Lab 2
# Date:             2023-04-14
# Description:      This program calculates net income.
# Input:            This program takes (float) gross income and (float) taxes
#                   as input.
# Output:           This program outputs (float) net income to the console.
# Sources:          Lab 2 specifications
#******************************************************************************

# What is your gross income for the time period? $100000
# What is your estimated effective tax rate? 25
# Your net income for the time period is: $75000

gross_income = 0.0
tax_rate = 0.0
tax_rate_percentage = 0.0
net_income = 0.0

print("Welcome to the Net Income Calculator!\n")
gross_income = float(input("What is your gross income for the time period?"
                           "\nS"))
tax_rate = float(input("\nWhat is your estimated effective tax rate?\n"
                       "Enter the percentage as a whole number (e.g. "
                       "25 for 25%)\n"))

tax_rate_percentage = tax_rate / 100
net_income = gross_income - (gross_income * tax_rate_percentage)

print(f"\nBased on your gross income and your effective tax rate, your net"
      f" income for the time period should be ${net_income:.2f}.")