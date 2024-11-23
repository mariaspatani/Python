"""
Author: Maria
Date:23/11/2024
This is a program to find roots of a quadratic equation
"""
import math
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
d=b*b-4*a*c
if d==0:
    root1=-b/(2*a)
    root2=root1
    print("Roots are real and Unequal")
    print("Root1 and Root2 are",root1 and root2)
elif d>0:
    root1=(-b+math.sqrt(d)/(2*a))
    root2=(-b-math.sqrt(d)/(2*a))
    print("Roots are unequal and distinct")
    print("Root1 and Root2 are",root1 and root2)
else:
    print("Roots are complex and imaginary")

