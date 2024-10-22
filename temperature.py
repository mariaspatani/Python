"""
author:maria
date:22/10/2024
version:1.1
This is a python program to convert temperature values back and forth between Celsius and Fahrenheit.
"""
temp=int(input("enter a temperature"))
unit=input("Is this in (C)elsius or (F)ahrenheit?")
if unit=='C':
    fahrenheit=((9/5*temp)+32)
    print(temp,"Celsius is",fahrenheit,"Fahrenheit")
else:
    Celsius=(5/9*(temp-32))
    print(temp, "Fahrenheit is", Celsius, "Celsius")



