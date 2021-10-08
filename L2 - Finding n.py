# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

numb = int(user_input)

sum = 0
i = 1

while sum < numb:
    sum += i
    i += 1

print(i - 1)