"""
Author: Maria
Date:22/11/2024
Version :1.1
This is a python program to check whether there are multiple maximum elements in a tuple.
"""
tuple1=(1,2,77,5,9,77,11,55,77,)
print(max(tuple1))
print(tuple1.count(max(tuple1)))
if tuple1.count(max(tuple1))==1:
    print("There is no multiple maximum elements in a tuple")
else:
    print("There are multiple maximum elements in a tuple ")


