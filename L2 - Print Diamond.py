# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
numb = int(input())

for i in range(0, numb // 2):
    for j in range(numb // 2, i, -1):
        print(" ", end = "")
    for j in range(0, 1 + i * 2):
        print("*", end = "")
    print("")
if numb % 2 == 1:
    for i in range(0, (numb // 2) * 2 + 1):
        print("*", end="")
    print("")
for i in range(0, numb // 2):
    for j in range(0, i + 1):
        print(" ", end = "")
    for j in range(0, (numb // 2 - 1 - i) * 2 + 1):
        print("*", end = "")
    print("")