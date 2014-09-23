#Hugo
#Math Unit Excercise 3
#23/09/14

import math
print("A plane travels 20km on a bearing of 060degrees.")

distance_east = math.sin(60) * 20
distance_north = distance_east * math.tan(30)

print("It travels {0}km north and {1}km east.".format(distance_north, distance_east))
