"""
Author:Maria
Date:30/11/2024
Version:1.1
This is a python program to check whether the triangle is a triangle.
"""
"""
Author:Maria
Date:30/11/2024
Version:1.1
This is a python program to check whether given sides are part of a right angled triangle .
"""

def triangle(length1,length2,length3):
    list1=[]
    list1.append(length1)
    list1.append(length2)
    list1.append(length3)
    print(list1)
    list1.sort()
    print(list1)
    if (list1[2]**2)==(list1[0]**2)+(list1[1]**2):
        print("The Triangle is a right angled triangle")
    else:
        print("The Triangle is not a right angled triangle")



length1=int(input("Enter the length of first side"))
length2=int(input("Enter the length of second side"))
length3=int(input("Enter the length of third side"))
triangle(length1,length2,length3)


