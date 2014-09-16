#Hugo
#Development Excercise 2
#16/09/14

import math

print("This is a Fehrenheit to Centrigrade converter")
fahren_temp = float(input("Please enter your temperature in degrees fahrenheit: "))
centi_temp_1 = fahren_temp - 32
centi_temp_2 = 5/9
centigrade = centi_temp_1*centi_temp_2
print("Your temperature in Centrigrade is {0}".format (centigrade))

