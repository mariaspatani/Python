"""
author : maria
date : 29/10/2024
version : 1.1
This is a python program to count number of vowel counts in a string.
"""


string_input=input ("Enter a string")
vowels="aeiouAEIOU"
vowels_count=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
print(f"No of Vowels in the given string {string_input}={vowels_count}")