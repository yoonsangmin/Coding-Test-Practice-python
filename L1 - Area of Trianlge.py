# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

base = int(user_input.split()[0])
height = int(user_input.split()[1])

print((base * height) / 2)