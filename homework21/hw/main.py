#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# Path: /Volumes/Samsung USB/Temp/py/nothing/requests!/Python Orginized/homework21/hw/main.py

def main():
    num = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    b = max(num, num2)
    while 1:
        if b % num == 0 and b % num2 == 0:
            print("Your number is: %d" % b)
            break
        b += max(num, num2)


if __name__ == '__main__':
    main()
