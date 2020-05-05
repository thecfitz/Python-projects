###############################################
# Colton Fitzjarrald
# 09/30/18
#
# step 1:
    # a) Create what's called a dictionary, a sort of variable-assignment bucket, to contain the values for multiple variables. This way, it's easy to reference that variable and get a value from it.
# step 2:
    # a) Prompt the user to enter a value for the car service they desire
    # b) It's important to account for the user misspelling some of the inputs, so creating what's called an if-else statement allows us to re-assign a value to the variable that the user might have messed up.
    # ^^(continued) It's important that the value we recieve as an input is specific, because we want to reference that 'dictionary' we made earlier, and we can't do that with misspelled words.
# step 3:
    # a) Creating another list of if-else statements allows us to reference that 'dictionary and output some values for the user. ie: costs.
    # ^^ We print the term 'you entered:', followed by whatever the user input was.
    # b) By referencing the input the user gave us, and by referencing our dictionary by the same input, the computer outputs the name of the service, as well as it's cost.
    # c) The final 'else' statement is in case the user inputs a word that isn't offered by the auto shop, and then they recieve an error message.
# step 4:
    # a) Using the values from the dictionary, we print out a list of all of the services and what they cost
# step 5:
    # a) We prompt the user to enter the two service they would like. and then we assign their input to two variables, in which we will then use if-else statements to account for any spelling errors, jsut like we did in step #2
    # b) We then create an invoice by adding the costs of each service, and assigning them to the variable 'total'. We the print 'total', and then the user knows how much it costs.
# step 6:
    # a) We ask the user to if they would like to add two more services, if yes, we repeat steps #3-5. If no, we print the phrase: 'Have a nice day'.
    # ^^ To account for the user using either 'Yes' or 'yes', etc. in their input, we again use if-else statements to re-assign their input.
################################################

# dictionary assigns the cost for each service
services = {'Oil change': 35,
            'Tire rotation': 19,
            'Car wash': 7,
            'Car wax': 12,
            'No service': 0}
# auto_serv is the user's desired car service
auto_serv = input('Desired auto service:')
# The following four 'if' statements are to allow the user multiple variances in spelling of desired auto service
if auto_serv == 'Tirerotation' or auto_serv == 'tirerotation':
    auto_serv = 'Tire rotation'
elif auto_serv == 'Oilchange' or auto_serv == 'oilchange':
    auto_serv = 'Oil change'
elif auto_serv == 'Carwash' or auto_serv == 'carwash':
    auto_serv = 'Car wash'
elif auto_serv == 'Carwax' or auto_serv == 'carwax':
    auto_serv = 'Car wax'

# the if-else statements are to give a result for each service the user requests
# the conversion specifiers throughout are for user aesthetics
if auto_serv == 'Tire rotation':
    print('You entered:', auto_serv)
    print('Cost of %s: $%d' % (auto_serv, services[auto_serv]))

elif auto_serv == 'Oil change':
    print('You entered:', auto_serv)
    print('Cost of %s: $%d' % (auto_serv, services[auto_serv]))

elif auto_serv == 'Car wash':
    print('You entered:', auto_serv)
    print('Cost of %s: $%d' % (auto_serv, services[auto_serv]))

elif auto_serv == 'Car wax':
    print('you entered:', auto_serv)
    print('Cost of %s: $%d' % (auto_serv, services[auto_serv]))

# the '\' and conversion specifiers are to reference the user's request with quotes around it.
else:
    print('Error: \'%s\' is not recognized' % auto_serv)

print('\n')

#the following 5 lines are to show the name of the autoshop and the services/prices
print('Python\'s auto shop services')
print('Oil change -- $%d' % services['Oil change'])
print('Tire rotation -- $%d' % services['Tire rotation'])
print('Car wash -- $%d' % services['Car wash'])
print('Car wax -- $%d' % services['Car wax'])
print('\n')

serv1 = input('Select first service:')
serv2 = input('Select second service:')
print('\n')
#the following two sets of if-else lines are to correct any spelling errors the user make make when inputting an auto service
# The last line of each if-else set is to allow the user to enter (-) for no service at a cost of $0
if serv1 == 'Tirerotation' or serv1 == 'tirerotation':
    serv1 = 'Tire rotation'
elif serv1 == 'Oilchange' or serv1 == 'oilchange':
    serv1 = 'Oil change'
elif serv1 == 'Carwash' or serv1 == 'carwash':
    serv1 = 'Car wash'
elif serv1 == 'Carwax' or serv1 == 'carwax':
    serv1 = 'Car wax'
elif serv1 == '-':
    serv1 = 'No service'
#In the case that the uses enters an incorrect input, the dictionary key 'No service' is assigned to the variable, so that the total invoice may still be calculated
else:
    print('Error: \'%s\' is not recognized' % serv1)
    serv1 = 'No service'

if serv2 == 'Tirerotation' or serv2 == 'tirerotation':
    serv2 = 'Tire rotation'
elif serv2 == 'Oilchange' or serv2 == 'oilchange':
    serv2 = 'Oil change'
elif serv2 == 'Carwash' or serv2 == 'carwash':
    serv2 = 'Car wash'
elif serv2 == 'Carwax' or serv2 == 'carwax':
    serv2 = 'Car wax'
elif serv2 == '-':
    serv2 = 'No service'
else:
    print('Error: \'%s\' is not recognized' % serv2)
    serv2 = 'No service'

print('Python\'s auto shop invoice')

print('\n')

print('Service 1: %s, $%d' % (serv1, services[serv1]))
print('Service 2: %s, $%d' % (serv2, services[serv2]))

total = services[serv1] + services[serv2]
print('Total: $%d' % total)

print('\n')

add_on = input('Would you like to add on two more services?')

print('\n')

# The following two sets of if-else statements repeat the code described in comment lines #54,55,56
if add_on == 'Yes' or add_on == 'yes':
    serv1 = input('Select first service:')
    serv2 = input('Select second service:')
elif add_on == 'No' or add_on == 'no':
    serv1 = 'No service'
    serv2 = 'No service'
    print('Have a nice day')
    
print('\n')


if serv1 == 'Tirerotation' or serv1 == 'tirerotation':
    serv1 = 'Tire rotation'
elif serv1 == 'Oilchange' or serv1 == 'oilchange':
    serv1 = 'Oil change'
elif serv1 == 'Carwash' or serv1 == 'carwash':
    serv1 = 'Car wash'
elif serv1 == 'Carwax' or serv1 == 'carwax':
    serv1 = 'Car wax'
elif serv1 == '-':
    serv1 = 'No service'
else:
    print('Error: \'%s\' is not recognized' % serv1)
    serv1 = 'No service'

if serv2 == 'Tirerotation' or serv2 == 'tirerotation':
    serv2 = 'Tire rotation'
elif serv2 == 'Oilchange' or serv2 == 'oilchange':
    serv2 = 'Oil change'
elif serv2 == 'Carwash' or serv2 == 'carwash':
    serv2 = 'Car wash'
elif serv2 == 'Carwax' or serv2 == 'carwax':
    serv2 = 'Car wax'
elif serv2 == '-':
    serv2 = 'No service'
else:
    print('Error: \'%s\' is not recognized' % serv2)
    serv2 = 'No service'
# the following 9-lines are to print the final invoice w/ total cost. The same code was used in lines #85-93
print('Python\'s auto shop invoice')

print('\n')

print('Service 1: %s, $%d' % (serv1, services[serv1]))
print('Service 2: %s, $%d' % (serv2, services[serv2]))

total = services[serv1] + services[serv2]
print('Total: $%d' % total)