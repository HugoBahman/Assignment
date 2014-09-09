#Hugo
#9/9/14
#Variable, Input, and Placeholder Practise

print("Hello!")
#print command will output what it's been told to in the brackets following it
first_name = input("What's your name: ")
#first_name is a variable and will be paired with whatever the user puts in
#input will take the user's input from whatever they type
#The green text in the speech marks will appear exactly as it's been typed
print(first_name)
#print here will take the first_name variable and show it to the user
print("Hi {0}! What's up?".format(first_name))
#print will show the user the what's between the first and last brackets
#"{0}" is a placeholder that will be replaced by whatever follows the .format
#.format(first_name) will bring up the first_name variable
