"""
Author:Maria
Date:30/11/2024
Version:1.1
This is a python program to check whether given number is a valid mobile number or not .
"""
number=input("Enter a number")
def valid_mobile_number():
    length=len(number)
    if length==10 and number[0] in "7 8 9":
        print("The given number is valid")
    else:
        print("the given number is not valid")
valid_mobile_number()

