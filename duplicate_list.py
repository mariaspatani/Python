"""
Author : Maria
Date : 19/11/2024
Version :1.1
This is a python program to input two list from the user and merge the two list that consist first elements should be even numbers and then odd numbers .

"""
list1=[]
list2=[]
list1_size = int(input("Enter a size of list1"))
list2_size =int(input("Enter the size of list2"))
for i in range(list1_size):
    list1.append(int(input("enter elements from list1")))
for i in range(list2_size):
    list2.append(int(input("enter elements from list2 ")))
print(list1,list2)
combined_list= list1+list2
print(combined_list)
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
even_list.sort()
odd_list.sort()
print(even_list)
print(odd_list)
merged_list= even_list+odd_list
print(merged_list)





