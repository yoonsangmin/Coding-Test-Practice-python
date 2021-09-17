# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

n = int(user_input)

for i in range(1, math.floor(n / 2) + 1):
    if n % i == 0:
        print(i, end=" ")

print(n, end=" ")