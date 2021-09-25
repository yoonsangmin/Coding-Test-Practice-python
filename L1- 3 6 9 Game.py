# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

count = 0

for i in range(1, int(user_input)):
    temp = i

    while temp > 0:
        units = temp % 10
        if(units % 3 == 0) and (units != 0):
            count += 1
        temp = int(temp / 10)

print(count)