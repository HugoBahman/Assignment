#Hugo
#Swimming Pool Volume
#19/09/14

print("This program will let you know how much water you need to fill a swimming pool once you enter the length, width, and depth of the shallow and deep ends. All values will be recorded in metres.")
pool_width = float(input("Please enter the width of your pool: "))
pool_length = float(input("Please enter the length of your pool: "))
shallow_depth = float(input("Please enter the depth of the shallow end: "))
deep_depth = float(input("Please enter the depth of the deep end: "))

section_a = pool_width*pool_length*shallow_depth
section_ba = pool_width*pool_length*deep_depth
section_bb = section_ba/2

total_volume = section_a+section_bb

print("You will need {0}mcubed of water to fill the pool.".format(total_volume))
