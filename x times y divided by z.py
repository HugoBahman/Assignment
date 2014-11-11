#Hugo Bahman
#12/09/14
#(x*y)/z

print("Hey! This program will take two numbers that you give it and divide the result of their multiplication by a third number!")
first_number = int(input("Please give your first number: "))
second_number = int(input("Please give your second number: "))
third_number = int(input("Please give your third number: "))
first_and_second_multiple = first_number*second_number

final_result = first_and_second_multiple/third_number

print("The answer is {0}!".format(final_result))
