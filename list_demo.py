"""
Author : Maria
Date : 19/11/2024
Version :1.1
This is a python program to remove duplicate element from a given list.

"""
original_list= [1,2,3,4,5,1,2,2,1,7,8,9,6,6]
unique_list=[]
for number in original_list:
    if number not in unique_list:
        unique_list.append(number)
print("The original list is", original_list)
print(unique_list)