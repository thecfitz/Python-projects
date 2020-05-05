# Colton Fitzjarrald
# 10/14/18
# This program serves as a calculator

#this function adds the value of var1 and var2
def add(x, y):
    return print('%d + %d =' % (var1, var2), x + y)
#this function subtracts the value of var1 and var2
def subtract(x, y):
    return print('%d - %d =' % (var1, var2), x - y)
#this function multiplies the value of var1 and var2
def multiply(x, y):
    return print('%d * %d =' % (var1, var2), x * y)
#this function divides the value of var1 and var2
def divide(x, y):
    return print('%d / %d =' % (var1, var2), x / y)
#this function modulizes the value of var1 and var2
def modulus(x, y):
    return print('%d %% %d =' % (var1, var2), x % y)
#this function exponentiates the value of var1 with var2
def power(x, y):
    return print('%d ** %d =' % (var1, var2), x ** y)

execution = 'yes'
while execution == 'Yes' or execution == 'yes' or execution == 'Y' or execution == 'y':
    print('\nSelect operation.')
    print(' 1. add\n 2. subtract\n 3. multiply\n 4. divide\n 5. modulus\n 6. power\n')
    calculation = int(input('Enter choice(1/2/3/4/5/6): '))
    print('\n')

    while 1 <= calculation <= 6:
        var1 = int(input('Enter first number: '))
        var2 = int(input('Enter second number: '))
        print('\n')
        if calculation == 1:
            add(var1, var2)
        elif calculation == 2:
            subtract(var1, var2)
        elif calculation == 3:
            multiply(var1, var2)
        elif calculation == 4:
            divide(var1, var2)
        elif calculation == 5:
            modulus(var1, var2)
        elif calculation == 6:
            power(var1, var2)
        else:
            print('Invalid input')
        execution = input('\n Do you want to continue?')
        if execution == 'No' or execution == 'no' or execution == 'N' or execution == 'n':
            break
        elif execution == 'Yes' or execution == 'yes' or execution == 'Y' or execution == 'y':
            break
        else:
            print('Invalid input \n')
            break
    else:
        print('Invalid input')
