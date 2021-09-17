# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

for i in range(int(user_input)):
    for j in range(int(user_input) - i - 1):
        print(" ", end="")
    for j in range(i * 2 + 1):
        print("*", end="")
    print("\n", end="")