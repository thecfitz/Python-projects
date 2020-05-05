######################################################
#Colton Fitzjarrald             9/13/2018
#
#problem1:

print('problem 1')
print('Enter a whole number: ', end='')
user_num1 = int(input())
print('Enter a second whole number: ', end='')
user_num2 = int(input())
print(user_num1, '/', user_num2, '= ', end='') #line added for user readability
print(round(user_num1/user_num2, 2))
######################################################

#problem 2:

print('problem 2')
print('Enter a number with one or more decimal places: ', end='')
user_num1 = float(input())
print('Enter another number with one or more decimal places: ', end='')
user_num2 = float(input())
print(user_num1, '/', user_num2, '= ', end='') #line added for user readability
print(round(user_num1/user_num2, 6))
#####################################################

#problem 3:

print('problem 3')
print('Enter a number with one or more decimal places: ', end='')
user_num1 = float(input())
print('Enter another number with one or more decimal places: ', end='')
user_num2 = float(input())
print(user_num1, '/', user_num2, '= ', end='') #line added for user readability
print('%.6E' % (user_num1/user_num2))

#####################################################

#problem 4:

print('problem 5:')
print('Enter an uppercase, or lowercase letter: ', end='')
user_letter = ord(input())
print('Code point equivalent: ', user_letter)

######################################################

#problem 5:

print('Problem 5:')
print('Enter any integer: ', end='')
x = int(input())
print('Enter another integer: ', end='')
y = int(input())
print(x, '+', y, '=', format(x+y, ',d'))
print(x, '-', y, '=', format(x-y, ',d'))
print(x, 'x', y, '=', format(x*y, ',d'))
print(x, '/', y, '=', round(x/y, 2))
print(x, '/', y, '(rounded to the lowest integer)= ', format(x//y, ',d'))
print('The remainder of ', x, '/ ', y, 'is: ', format(x%y, ',d'))
print(x, '^', y, '= ', format(x**y, ',d'))