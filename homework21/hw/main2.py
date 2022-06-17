#!/usr/bin/python3
# -*- coding: utf-8 -*-


n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

smaller = min(n1, n2)
for i in range(smaller, 0, -1):
    if n1 % i == 0 and n2 % i == 0:
        print(n1 * n2 // i)
        break


