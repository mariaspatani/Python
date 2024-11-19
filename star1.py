"""
Author : Maria
Date ; 19/11/2024
Version : 1.1
This is a python program that perform increasing triangular pattern.
"""
n=int(input("Enter row number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*', end=" ")
    print(" ")

