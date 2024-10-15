"""
Python program to determine the entry ticket fare in a zoo based on age.
Version 1.1
Date 15/10/2024
"""
Age= int(input("enter age"))
if Age<10:
    print("Fare is 7")
elif Age>=10 and Age<60:
    print("Fare is 10")
else:
    print("Fare is 5")
