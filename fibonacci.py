"""
Author: Maria
Date: 2/12/2024
Version:1.1
This is a python program to find fibonacci numbers
"""
N=int(input("Enter a number"))
number1=0
number2=1
count=0
print(number1,end=" ")
print(number2,end=" ")
while count<N:
    result =number1+number2
    print(result,end=" ")
    number1=number2
    number2=result
    count=count+1
