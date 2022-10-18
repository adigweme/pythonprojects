# import sys in order to use sys functions
import sys

# establish variables to be used within script
without_space = 0
with_space = 0
result = []
parsed_specials = 0
total_specials = 0

# identify special characters
specials = [ ",", "-", ".", "?", "=", "!", ";", "+", ":"]
print("Welcome to Character Counter.")
print("Please input your text.")    
print(">>>")
init = input()

# main if statement to handle scanning user inputted text
if len(init)>1:
   n = len(init)
   for n in range(0, n):
# count characters and words in this next block
        with_space +=int(len(init[n]))
        without_space = with_space - init.count(' ')
# output results of character count and word count.
   print("")
   print("Total character count, without spaces, is", without_space)
   print("Total character count, with spaces, is", with_space)
# turn user input into a string
   string =  str(init)
# for loop to iterate through special characters, searching user input, getting total number and creating list of characters
   for char in specials:
        if char in string:
            result += char
            total_specials = total_specials + string.count(char)
        else:
            continue
# parse input to identify word count 
   word_parse = init.split(' ')
# ensure no special characters are included in word count
   for char in specials:
        if char in word_parse:
            parsed_specials = parsed_specials + word_parse.count(char)
        else:
            continue
   words = int(len(word_parse)) - int(parsed_specials)
   print("Total word count is", words)
# if statement to allow user to choose whether to print special characters
   if len(result) > 0:
        print("Found", total_specials, "instances of", len(result), "special character(s)")
        print("Do you want to see special character(s)? [Y / N]")
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
