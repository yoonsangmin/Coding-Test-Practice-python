# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import collections

user_input = input()

choices = user_input.split()

winner_count = 0

dic = {1 : 0, 2 : 0, 3 : 0}

for i in choices:
    dic[int(i)] += 1

if dic[1] == len(choices) or dic[2] == len(choices) or dic[3] == len(choices):
    winner_count = 0
elif dic[1] * dic[2] * dic[3] != 0:
    winner_count = 0
else:
    if dic[3] == 0:
        winner_count = dic[2]
    elif dic[2] == 0:
        winner_count = dic[1]
    elif dic[1] == 0:
        winner_count = dic[3]


print(winner_count)