import re

#Instructions on how to use and Grades convertion table
print('GRADE LIST \n=======================\nA = 4.00 grade points \nA- = 3.70 grade points \nB+ = 3.33 grade points \nB = 3.00 grade points \nB- = 2.70 grade points \nC = 2.00 grade points \nC- = 1.70 grade points \nD+ = 1.30 grade points \nD = 1.00 grade points \nD- = 0.70 grade points \nF = 0 grade point \n=======================\n')
print('INSTRUCTION \n=======================\nGrades must be letter, seperated by spaces. Credit hours must be integer, seperated by spaces\n=======================\n')

#Dictionary to store letter grades as their value
gradebook = {'A': 4.00, 'A-': 3.70, 'B+': 3.33, 'B': 3.00, 'B-': 2.70, 'C+': 2.30, 'C': 2.00, 'C-': 1.70, 'D+': 1.30, 'D': 1.00, 'D-': 0.7, 'F': 0}


#Inputting grades as a whole string. Prompt is made if the format is wrong
#Loop continue to take input as long as input is in wrong format
while True:
    grades = input("What's your grade(s)? \nMy grades are: ")
    grades = grades.split()
    temp = 0
    for grade in grades:
        if grade in gradebook.keys():
            temp = temp + 1
    if temp == len(grades):
        break
    else:
        print('>>> Wrong grade format, try again!')


#Inputting credit hours as a whole string. Prompt is made if either the format is wrong
#or number of credit hours doesn't match with the number of grades
#Loop continue to take input as long as input is in wrong format
while True:
    weights = input("What's your credit hour(s), respectively? \nMy credit hours are: ")
    #if input string contains anything more than whitespaces and digits from 0-9, it must not
    #contains integers only and vice versa
    if re.search('[^0-9\s]', weights):
        print('>>> Wrong credit hour(s) format, must be Integer. Try again!')
    else:
        weights = weights.split()
        if len(weights) != len(grades):
            print('>>> Your number of credit hours does not match the number of grades. Try again!')
        else:
            break

#Making a list to store credit hours as integer and a list to store the 'weights'
#of each score according to its credit hours
weightlist = []
final = []


for weight in weights:
    weightlist.append(int(weight))

#Calculating the sum of all scores and their corresponding credit hours
for i in range(len(grades)):
    final.append(gradebook.get(grades[i])*int(weights[i]))


#Printing the final GPA, rounding to two decimal places
print('Your GPA is:', round(sum(final)/sum(weightlist), 2))
