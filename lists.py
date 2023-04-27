'''
PIC 16A Homework 1
Author: Michelle Pan
UID: 105623333
Discussion Section: 3B
Date: 04/16/2023
'''
# First list
list1 = [[i for i in range(j+1)] for j in range(5)]
print(list1)

# Second list
list2 = [i for j in range(5) for i in range(j+1)]
print(list2)

# Third list
list3 = [i*5 + 5 for i in range(1, 7)]
print(list3)

# Fourth list
list4 = ([i for i in range(65, 10, -10)])
print(list4)

