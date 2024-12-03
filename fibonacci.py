"""
Author:Maria
Date:3/12/2024
Version:1.1
This is  a python program to generate fibonacci number.
"""
def generate_fibonacci(n):
    number1=1
    number2=0
    number3=0

    count=0
    while count<n:
        print(number3, end=" ")
        number3=number1+number2

        number1= number2
        number2=number3
        count+=1

(generate_fibonacci(10))

