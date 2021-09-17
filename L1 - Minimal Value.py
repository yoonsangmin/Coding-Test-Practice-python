# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

# nums = list(map(int, user_input.split()))
# nums = map(int, user_input.split())
nums = [int(i) for i in user_input.split()]

print(min(nums))