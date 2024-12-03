"""
Author:Maria
Date:3/12/2024
Version:1.1
This is  a python program to find factorial of a number using recursion.
"""
def factorial (n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(5)
print(result)

