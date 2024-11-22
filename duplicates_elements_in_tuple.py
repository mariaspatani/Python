"""
Author: Maria
Date: 22/11/2024
Version:1.1
This is a python program to check whether duplicate elements present in a tuple.
"""
original_tuple=(1,2,3,3,5,8,9,9,5,1,3)
unique_tuple=()
#convert tuple into list
list1= list(original_tuple)
list2=list(unique_tuple)
print(list1)
print(list2)
for element in list1:
    if element not in list2:
        list2.append(element)
print("original list:",list1)
print("list without duplicates:",list2)
#convert list1 and list2 into tuple
print("original_tuple",tuple(list1))
print("Tuple without duplicates",tuple(list2))
#check whether tuple contains duplicate element or not
if tuple(list1)==tuple(list2):
    print("No duplicate elements present in tuple")
else:
    print("Duplicate elements  present in tuple")

