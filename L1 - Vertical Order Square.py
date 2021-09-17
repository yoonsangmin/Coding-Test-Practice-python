# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

n = int(user_input)

for i in range(1, n + 1):
    for j in range(i, i + n * (n - 1) + 1, n):
        print(j, end=" ")
    print("\n", end="")