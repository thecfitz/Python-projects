# Colton Fitzjarrald
#
# This program takes all of the students' grades on exams, tests, and quizzes, and assigns them their class grades based on weighted averages. It also, calculates the class average as well.
#Below is not an algorithm, but a very brief description of how the code is organized
# step 1:
#   Create a dictionary that contains all the students grades for their homework, quizzes, and tests.
#   Create a list that refers to the names of the dictionaries and create a for loop that prints all the values of the dictionary keys.
# step 2:
#   Create functions that serve as the main tools for the program. Some interlink with each other to provide ease.

harry = {
 "name": "Harry",
 "homework": [90.0, 97.0, 75.0, 92.0],
 "quizzes": [88.0, 40.0, 94.0],
 "tests": [75.0, 90.0]
}
zayn = {
 "name": "Zayn",
 "homework": [100.0, 92.0, 98.0, 100.0],
 "quizzes": [82.0, 83.0, 91.0],
 "tests": [89.0, 97.0]
}
niall = {
 "name": "Niall",
 "homework": [0.0, 87.0, 75.0, 22.0],
 "quizzes": [0.0, 75.0, 78.0],
 "tests": [100.0, 100.0]
}

#prints all values in dictionaries
students = [harry, zayn, niall]
for student in students:
    for key, values in student.items():
        print(values)
print()

# function below calculates averages
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total/len(numbers)


# get_average returns the weighted average of each student
def get_average(student):
    homework = average(student["homework"])
    homework *= .1
    quizzes = average(student["quizzes"])
    quizzes *= .3
    tests = average(student["tests"])
    tests *= .6
    weights = [homework, quizzes, tests]
    return sum(weights)


# function below assigns letter grade to students
def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


#print letter grades
for student in students:
    print('%s letter grade: ' % student['name'], end='')
    print(get_letter_grade(get_average(student)))
print()

# function below returns the class average
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)


# prints the class average and letter grade
print('Class average is: ', round(get_class_average(students), 2))
print('Letter grade -average: %s' % get_letter_grade(get_class_average(students)))
