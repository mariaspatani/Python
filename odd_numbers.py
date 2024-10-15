"""
Python program to generate  n odd numbers.
Version 1.1
Date : 15/10/2024
"""
limit= int(input("enter the limit:"))
count=0
odd_number =1
while count<limit:
    print(odd_number, "\t",end="")
    count+=1
    odd_number+=2