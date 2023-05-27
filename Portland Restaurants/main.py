# *****************************************************************************

import valid as v
import sys

def main():
	"""
	This program is used to store rating information about restaurants
	in the Portland area
	"""
	restaurants = []
	ratings = []
	genres = []
	more = "y"
	start = ""

	greetings()
	start = getting_started()
	start_or_not(start)
	while more == 'y':
		list_builder(restaurants, ratings, genres)
		more = enter_more()



# *********************** Inputs ****************************************

def getting_started():
	"""
	This function lets the user indicate they're ready to begin.
	"""
	start = ""

	start = v.get_y_or_n("Are you ready to begin? (y or n): ")
	return start

def list_builder(restaurants, ratings, genres):
	"""
	This function takes input for the lists.
	"""
	restaurant = ""
	rating = ""
	genre = ""

	restaurant = v.get_string("\nPlease enter the name of the restaurant: ")
	restaurants.append(restaurant)
	rating = v.get_integer("Please enter a rating (1 - 5) for the restaurant: ")
	ratings.append(rating)
	genre = v.get_string("What genre is this restaurant's food? ")
	genres.append(genre)

def enter_more():
	"""
	Determine if user would like to continue to add values to lists
	"""
	more = ""

	more = v.get_y_or_n("\nWould you like to enter another restaurant? (y or n) ")
	return more


# *********************** Calculations and Selections ********************

def start_or_not(start):
	"""
	this function determines whether or not the program executes.
	:param start: User decision as a string (y/n)
	"""
	if start == "y":
		return
	else:
		sys.exit()

# *********************** Outputs ****************************************

def greetings():
	"""
	This function greets the user.
	"""
	print("Welcome to the Restaurant Rater. You can enter a rating and"
		"genre for a given restaurant and query your list once completed.")


# *********************** Main Run ****************************************
main()