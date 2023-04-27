'''
PIC 16A Homework 1
Author: Michelle Pan
UID: 105623333
Discussion Section: 3B
Date: 04/16/2023
'''
def squareUpTo(n):
    squareNumbers = [x ** 2 for x in range(0, n) if x ** 2 <= n]
    print(squareNumbers)

