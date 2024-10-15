"""
author: maria
Version 1.1
Date: 15/10/2024
Python program to generate sum of digits
"""
number=int(input("enter a number"))
sum=0
while number>0:
    r= number%10
    number= number//10
    sum= sum+r
print("The sum of the digits is",sum)
