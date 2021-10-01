# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
num = int(user_input)

sum = (1 + num) * num // 2 % 1000000007

answer = (sum * sum) % 1000000007

print(answer)