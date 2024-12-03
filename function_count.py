"""
Author:Maria
Date:3/12/2024
Version: 1.1
This is a python program to find the number of lower case and upper case characters in a string.
"""
def count_upper_lower_case_character(input_string):
    upper_characters_count =0
    lower_characters_count=0
    for character in input_string:
        if character.isupper():
           upper_characters_count +=1
        elif character.islower():
            lower_characters_count +=1
    return upper_characters_count,lower_characters_count


input_string1=input("Enter the string")
upper_character_count,lower_characters_count=count_upper_lower_case_character(input_string1)
print(upper_character_count)
print(lower_characters_count)
