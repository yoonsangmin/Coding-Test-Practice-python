# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

numb = int(user_input)

percentage = 0

if numb < 100:
    percentage = 0.5
elif numb < 200:
    percentage = 0.7
elif numb < 300:
    percentage = 0.9
else:
    percentage = 1

print('{:.2f}'.format(numb * percentage / 100))