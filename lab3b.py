#########################################
# Colton Fitzjarrald
# 9/20/18
    # step 1:
        # a) Prompt user to enter name of food using "print()"
        # b) Define the various inputs by the user, using the term "input()"
        # c) Prompt user to enter price, and use "float()" to account for any decimal value the user might enter
        # d) Prompt user to enter the number of items purchased, and use "int()" to ensure the value is a whole number
    # step 2:
        # a) repeat step 1
    # step 3:
        # a) Calculate the total cost of each food item by multiplying the item price by the amount of that item purchased
        # b) Calculate the total cost for all food items by adding the total cost for each food item
    # step 4:
        # a) Print the receipt: number of item purchased, name of item, item price, and total cost for item. Do this for both items, and include the total cost below.
        # b) define gratuity as the total cost multiplied by 15%
        # c) print the gratuity
        # d) print the total bill by adding the gratuity to the total cost
###########################################

print('Enter food item name:')
food1 = input()
print('Enter item price:')
food1_price = float(input())
print('Enter number of items purchased (only whole numbers allowed):')
food1_amount = int(input())
food1_totalcost = food1_amount*food1_price #multiplying the amount of food1 by the price of food1 gives total cost
print('Enter second food item name:')
food2 = input()
print('Enter item price:')
food2_price = float(input())
print('Enter number of items purchased: (only whole numbers allowed):')
food2_amount = int(input())
food2_totalcost = food2_amount*food2_price #multiplying the amount of food2 by the price of food2 gives total cost
total_cost = food1_totalcost + food2_totalcost
print('\n') #The multiple print('\n') lines in the code is for aesthetics
print('RECEIPT')
print(food1_amount, food1, '@ $', food1_price, '= $', food1_totalcost)
print(food2_amount, food2, '@ $', food2_price, '= $', food2_totalcost)
print('Total cost: $', total_cost)
print('\n')
gratuity = total_cost*.15
print('15% gratuity: $', gratuity)
print('Total with tip: $', round(gratuity + total_cost, 2)) #rounding allows the total cost to be a conventional amount