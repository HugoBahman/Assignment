#Hugo
#Development Excercise 3
#16/09/14

print("This program takes your height and weight in inches and stones and then converts them to cm and kg.")
inches_height = float(input("Please enter your height in inches: "))
stones_weight = float(input("Please enter your weight in stones: "))
cm_height = inches_height*2.54
kg_weight = stones_weight*6.364
print("You are {0}cm tall and weigh {1}kg".format(cm_height, kg_weight))
