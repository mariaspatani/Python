"""
Author:Maria
Date:3/12/2024
Version:1.1
This is  a python program to find gcd of  numbers using recursion.
"""
def gcd_numbers(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd_numbers(n2,n1%n2)
result=gcd_numbers(1220,516)
print(result)
