# 1번
# # -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean
# user_input = input()
# # print ("Hello Goorm! Your input is " + user_input)
#
# print(user_input.replace(" ", ""))

# 2번
import re

user_input = input()

user_input = re.sub(r"\s+", "", user_input)

print(user_input)

# 3번
# user_input = input()
#
# user_input =  ''.join(user_input.split())
#
# print(user_input)