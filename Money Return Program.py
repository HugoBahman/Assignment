#Hugo
#Money Return Program
#19/0/14

print("This program will take an amount of money that you put in and return what change you can expect. This only works will whole pounds.")
total_money = int(input("Please enter how much money you have: "))
amount_of_20 = (total_money // 20)
twenty_remainder = (total_money % 20)
amount_of_10 = (twenty_remainder // 10)
ten_remainder = (twenty_remainder % 10)
amount_of_5 = (ten_remainder // 5)
five_remainder = (ten_remainder % 5)
amount_of_2 = (five_remainder // 2)
two_remainder = (five_remainder % 2)
amount_of_1 = (two_remainder // 1)


print("You will have {0} £20 notes, {1} £10 notes, {2} £5 notes, {3} £2 coins, and {4} £1 coins.".format(amount_of_20, amount_of_10, amount_of_5, amount_of_2, amount_of_1))

      
