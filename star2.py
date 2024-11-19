"""
Author : Maria
Date : 19/11/2024
Version :1.1
This is a python program to perform a decreasing triangular pattern.

"""


n= int(input("Enter a row number"))
for i in range(n):
    for j in range(n-i):
        print('*', end=" ")
    print(" ")