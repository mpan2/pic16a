'''
PIC 16A Homework 2
Author: Michelle Pan
UID: 105623333
Discussion Section: 3B
Date: 04/23/2023
'''
import math

def solve(f, fPrime, x_0, epsilon):
    xn = x_0
    error = abs(f(xn))
    
    while error > epsilon:
        xn = xn - f(xn) / fPrime(xn)
        error = abs(f(xn))
    return xn

# test 1
f1 = lambda x: x**2 - 1
f1_prime = lambda x: 2*x
x0_1 = 3
epsilon_1 = 0.0001
root_1 = solve(f1, f1_prime, x0_1, epsilon_1)
print(root_1)

# test 2
f2 = lambda x: x**2 - 1
f2_prime = lambda x: 2*x
x0_2 = -1
epsilon_2 = 0.0001
root_2 = solve(f2, f2_prime, x0_2, epsilon_2)
print(root_2)

# test 3
f3 = lambda x: math.exp(x) - 1
f3_prime = lambda x: math.exp(x)
x0_3 = 1
epsilon_3 = 0.0001
root_3 = solve(f3, f3_prime, x0_3, epsilon_3)
print(root_3)

# test 4
f4 = lambda x: math.sin(x)
f4_prime = lambda x: math.cos(x)
x0_4 = 0.5
epsilon_4 = 0.0001
root_4 = solve(f4, f4_prime, x0_4, epsilon_4)
print(root_4)
