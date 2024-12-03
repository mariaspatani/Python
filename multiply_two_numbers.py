"""
Author:Maria
Date:3/12/2024
Version:1.1
This is  a python program that add multiply positive numbers using recursion.
"""
def multiply_two_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multiply_two_numbers(n1,n2-1)
result= multiply_two_numbers(4,3)
print(result)