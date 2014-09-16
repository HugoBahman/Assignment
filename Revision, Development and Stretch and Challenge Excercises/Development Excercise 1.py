#Hugo
#Development Excercise 1
#16/09/14

print("This program will divide and give you the remainder for two numbers that you put in")
first_number = float(input("Please enter your first number: "))
second_number = float(input("Please enter your second number: "))
divided_number = float(first_number // second_number)
remainder = first_number % second_number
print("Your answer is {0} with a remainder of {1}".format(divided_number,remainder))
