# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

user_input = input()
wave_pos = list(map(int, user_input.split()[0:2]))
r = float(user_input.split()[2])

sensors = []
user_input = input()
sensors.append(list(map(int, user_input.split())))
user_input = input()
sensors.append(list(map(int, user_input.split())))
user_input = input()
sensors.append(list(map(int, user_input.split())))
user_input = input()
sensors.append(list(map(int, user_input.split())))
user_input = input()
sensors.append(list(map(int, user_input.split())))

answer = -1

min_dist = r

for i in range(0, len(sensors)):
    a = sensors[i][0] - wave_pos[0]
    b = sensors[i][1] - wave_pos[1]
    dist = math.sqrt((a * a) + (b * b))
    if dist <= r and dist <= min_dist:
        min_dist = dist
        answer = i + 1

print(answer)