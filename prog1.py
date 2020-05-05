####################################
#colton fitzjarrald
# 10/9/18
##
# step 1:
    # a) We ask the user to enter a four digit number, and then we turn that number into a collection of integers, organized by their position in the number
    # b) by taking this collection of numbers inputted by the user, we can compare them to the combination and evaluate each integer for it's accuracy
# step 2:
   # a)for every number the user enters that's incorrect, there's a set of instructions that are separate from the instructions if the user enters the correct number
    # if the user enters the correct number, we say they broke the vault and it took them 1 try
# step 3:
    # a) The separate set of instructions we follow, mentioned in step 2(a), tell the computer to compare the value of each digit with respect to it's position, for both the combination and the user's input.
    # b) We compare whether each digit is greater than, less than, or equal to each other, and then we tell the computer to count the amount of each inequality.
    # c) we then give the user a clue to the combination by telling them how their number compared with the combination's by giving them the inequalities
# step 4:
    # a) The user continues to alter their input by the inequalities we give them, until they get the correct answer. We then divert to the first set of instructions, which is to tell them they broke the vault, and they have tried x-times.

###########################################


# by putting the combination to the vault into a list, it allows an index comparison with the user's input.
combination = [1, 2, 3, 4]
user_num = input('Guess the combination(four digits):')
# line 25 is to turn the user's input into a list of integers.
user_num = [int(user_num[0]), int(user_num[1]), int(user_num[2]), int(user_num[3])]

try_num = 1
# the user enters a 4 digit number, the while loop sends any incorrect number to the for loop.
while user_num != combination:
    equal_num = 0
    less_num = 0
    great_num = 0
# the for loop cycles i for the range of the length of the stored combination.
    for i in range(len(combination)):
# The if-else statements compare the value of each index of each list, i being the index. In each case, the accumulators increment below the if-else statements.
        if user_num[i] == combination[i]:
            equal_num += 1
        elif user_num[i] < combination[i]:
            less_num += 1
        elif user_num[i] > combination[i]:
            great_num += 1
#the try_num variable is to count the number of tries the user inputs. The loop increments with each try.
    try_num += 1
    print('Nope! Your clue is: ', end='')
# line 46 gives the multiple of the associated inequality signs to give the user a clue
    print(equal_num * '= ' + less_num * '< ' + great_num * '> ')

    user_num = input('Guess the combination(four digits): ')
# since there is a second input by the user, user_num must be redefined as a list of integers.
    user_num = [int(user_num[0]), int(user_num[1]), int(user_num[2]), int(user_num[3])]
# line 52 is for user aesthetics
print('\n')

print('You broke the vault!', 'You took %d tries to break the vault.' % try_num)

