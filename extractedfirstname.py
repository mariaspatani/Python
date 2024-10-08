"""
program name : extracting first name
version: 1.1
date: 8-10-2024
This is a python program that create two separate strings,concatenating string,from the concatenated string:
Access and print a sub-string that consists of the first name only.
"""



first_name= input("enter your first name")
last_name= input("enter your last name")
full_name= first_name+ " "+ last_name
print(full_name)
length= len(first_name)
print(length)
extracted_first_name= full_name[:length]
print(extracted_first_name)