# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
sentence = user_input

user_input = input()
start = int(user_input.split()[0]) - 1
lenth = int(user_input.split()[1])


print(sentence[start:start + lenth])