"""
author:maria
date:29/10/2024
version:1.1
This python program is to check whether the given number is prime or not.
"""

check_prime=int(input("enter a number"))
for i in range(2,(check_prime//2)+1):
    print(f"Value of i{i} and {check_prime}%{i}={check_prime%i}")
    if check_prime%i==0:
        break
if i==(check_prime//2):
    print(f"The given number {check_prime} is prime")
else:
    print(f"The given number {check_prime} is mot prime")