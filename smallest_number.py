"""
Python program to determine the smallest of  three numbers.
Version 1.1
Date - 15/10/2024
"""
number1= int(input("enter first number"))
number2= int(input("enter second number"))
number3= int(input("enter third number"))
if number1<number2 and number1<number3:
    print(number1)
elif number2<number1 and number2<number3:
    print(number2)
else:
    print(number3)