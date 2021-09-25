# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

limit = int(user_input)

sum = 0

for i in range(3, limit + 1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

'''
for i in range(3, limit + 1, 3):
    sum += i

for i in range(5, limit + 1, 5):
    sum += i

for i in range(15, limit + 1, 15):
    sum -= i
'''

print(sum)