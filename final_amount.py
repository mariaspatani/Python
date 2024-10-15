"""
Python program to calculate the final amount after applying discount.
Version 1.1
date 15/10/2024
"""
purchase_amount=int(input("enter the purchase amount"))
if purchase_amount>500:
    discount= purchase_amount*0.2
    final_amount= purchase_amount-discount
    print(final_amount)
elif purchase_amount>=200 and purchase_amount<=500:
    discount= purchase_amount*0.1
    final_amount= purchase_amount-discount
    print(final_amount)
else:
    final_amount=purchase_amount
    print(final_amount)