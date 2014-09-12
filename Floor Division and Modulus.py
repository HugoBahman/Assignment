#Hugo Bahman
#12/09/14
#Floor Division and Modulus

print("Hey! This program takes two numbers and divides them to give a whole number and remainder!")
first_number = input("Please enter your first number: ")
second_number = input("Please enter your second number: ")

floor_division = first_number//second_number
modulus = first_number%second_number
print("Your answer is {0}{1}!".format(floor_division,modulus))
