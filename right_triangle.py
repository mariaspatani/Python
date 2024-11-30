"""
Author:Maria
Date:30/11/2024
Version:1.1
This is a python program to check whether given sides are part of a right angled triangle .
"""

def is_right_angle_triangle(side1,side2,side3):
    """
    Function to check right angle triangle
    :param side1: side1 of the triangle
    :param side2: side2 of the triangle
    :param side3: side3 of the triangle
    :return: True, if the sides are part of a right angle triangle ,False otherwise
    """
    sides =[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[0]**2 + sides[1]**2:
        return True
    return False
side1=int(input("enter side1"))
side2=int(input("enter side2"))
side3=int(input("enter side3"))
if is_right_angle_triangle(side1,side2,side3):
    print("The Triangle is a right angled triangle")
else:
    print("The Triangle is not a right angled triangle3")