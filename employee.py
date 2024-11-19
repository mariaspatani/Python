"""
Author : Maria
Date : 19/11/2024
Version :1.1
This is a python program about employee information.

"""

employee_information= [
    ("Ajay","A",20000.00),
    ("Deepak","B",60000.00),
    ("Sherin","C",70000.00),
    ("Manoj","D",50000.00)
]
sum=0

threshold= float(input("enter threashold"))
for i in employee_information:
    employee_name,department,monthly_salary= i
    if i[2]> threshold:
        print(employee_name)
    sum+=i[2]
print(sum*12)


