"""
Author : Maria
 Date ; 19/11/2024
 Version : 1.1
 This is a python program that perform increasing hill pattern.
"""
n= int(input("Enter a row number"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print('*',end=" ")
    print()


