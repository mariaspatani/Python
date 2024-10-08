"""
program name : Arithmetic Operations
version: 1.1
date: 8-10-2024
This is a python program that performs addition , subtraction, multiplication,division, modulus,combined operations
"""


number1= int(input("enter the first number"))
number2= int(input("enter the second number"))
number3= int(input("enter the third number"))
A= number1+number2
print("The sum of num1 and num2 is",A)
B= number2-number1
print("The difference when num2 is subtracted from num2 is",B)
C= number1*number2
print("The product of num1 and num2 is",C)
D= number1/number2
print("The quotient when num1 is divided by num2 is",D)
E= number1%number2
print("The remainder when num1 divided by num2",E)
F= (number1+number2)*number3/2
print("The result of (num1 + num2) * num3 / 2 is",F)