"""
Author:Maria
Date:3/12/2024
Version:1.1
This is  a python program that add two positive numbers using recursion.
"""
def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
result=add_numbers(5,4)
print(result)
