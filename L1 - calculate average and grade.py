# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

sum = int(user_input.split()[0]) + int(user_input.split()[1]) +int(user_input.split()[2])
average = round(sum / 3, 2)
grade: chr

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("{:.2f}".format(average) + " " + grade)