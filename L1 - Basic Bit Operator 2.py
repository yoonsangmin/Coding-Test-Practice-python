# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

a = int(user_input.split()[0])
b = int(user_input.split()[1])

print(a >> b)
print(a << b)