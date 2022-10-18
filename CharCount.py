# import sys in order to use sys functions
import sys

# establish variables to be used within script
add = 0
with_space = 0
result = []
init = input()

# main if statement to handle scanning user inputted text
if len(init)>1:
   n = len(init)
   for n in range(1, n):
# count characters and words in this next block
        without_space +=int(len(init[n]))
        with_space = add + init.count(' ')
        words = init.count(' ') + 1
# output results of character count and word count.
   print("Total character count, without spaces, is", without_space)
   print("Total character count, with spaces, is", with_space)
   print("Total word count is", words)
# turn user input into a string
   string =  str(init)
# identify special characters
   specials = [ ",", "-", ".", "?", "=", "-", ";", "+", ":"]
# for loop to iterate through special characters, searching user input
   for char in specials:
        if char in string:
            result += char
        else:
            continue
# if statement to allow user to choose whether to print special characters
   if len(result) > 0:
        print("Found", len(result), "special characters")
        print("Do you want to see special characters? [Y / N]")
        input= input()
        if input == "Y" or input == "y" or input == "yes":
            print("Here you go:")
            print(result)
            print("Okay, thanks for using the Character Counter.")
        elif input == "N" or input == "n" or input == "no":
            print("Okay, thanks for using the Character Counter.")
        else:
            print("invalid selection")
   else:
        print("No special characters found.")
else:
    print("invalid arguments")
