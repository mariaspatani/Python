"""
Author : Maria
 Date ; 19/11/2024
 Version : 1.1
 This is a python program that perform reverse hill pattern pattern.
"""


n= int(input("Enter a row number"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print('*',end=" ")
    print()