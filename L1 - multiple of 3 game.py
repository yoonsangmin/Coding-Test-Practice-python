# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

for i in range(1, int(user_input) + 1):
    if i % 3 == 0:
        print('X', end=" ")
    else:
        print(i, end=" ")