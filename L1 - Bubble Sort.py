# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()

max = int(user_input.split()[0])

user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

nums = list(map(int, user_input.split()[0 : max]))

for i in range(len(nums) - 1, 0, -1):
    for j in range(0, i):
        if(nums[j] > nums[j + 1]):
            nums[j], nums[j + 1] = nums[j + 1], nums[j]


for num in nums:
    print(num, end=" ")