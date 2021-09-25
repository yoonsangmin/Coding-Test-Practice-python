# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from functools import reduce

user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

arr = list(map(int, user_input.split()))

multiply = reduce(lambda a, b: a * b, arr)

print(multiply)