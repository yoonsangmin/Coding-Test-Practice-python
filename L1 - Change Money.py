# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

price = int(user_input)
change = 1000 - price

count_500 = int(change / 500)
change %= 500
count_100 = int(change / 100)
change %= 100
count_50 = int(change / 50)
change %= 50
count_10 = int(change / 10)

print(count_500, count_100, count_50, count_10, end=' ')