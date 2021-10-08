# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

numb = int(user_input)

result = True

for i in range(2, int(math.sqrt(numb) + 1)):
    if numb % i == 0:
        result = False

print(result)
