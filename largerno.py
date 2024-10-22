"""
author:maria
date:22/10/2024
version:1.1
This is a python program to find the largest of three numbers.

"""
number1=int(input("enter the first number"))
number2=int(input("enter the second number"))
number3=int(input("enter the third number"))
if number1>number2 and number1>number3:
    print(number1)
elif number2>number1 and number2>number3:
    print(number2)
else:
    print(number3)
