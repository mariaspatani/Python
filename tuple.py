#CLASSROOM EXERCISES

fruits=("banana","apple","cherry","date",)
print(fruits[0])
print(fruits[-1])
print(fruits[-2])
print(len(fruits))

#concatenation
tuple1=(1,2,3,"A","B","C",)
tuple2=(9,8,7,"Z","Y","X",)
tuple3= tuple1+tuple2
print(tuple3)

#Repeating
repeat_element=("python",)*5
print(repeat_element)
#Slicing
colors= ("red","yellow","blue","green","black",)
print(colors[0:3])
print(colors[1:4])
print(colors[-2:])
#unpack tuple into variables
person =("Alice", 25,"Engineer",)
name, age,profession =person
print(name)
#Problem1
"""
Author: Maria
Date:19/11/2024
Version:1.1
This is a python program to find highest value of an item from given items.
"""
inventory =[
    ("Laptop", 5, 30000.00),
    ("Headphone",15, 500.00),
    ("Mouse",50,150.00),
    ("Keyboard",20,150.00),
    ("Monitor",10,5000.00)
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,unit_price =item
    stock_value =quantity*unit_price
    print(f"Item Name:-{item_name},the stock_value is: {stock_value}")
    if stock_value> highest_stock_value:
        highest_stock_value= stock_value
        item_with_highest_stock_value=item_name
    print(f"Highest stock value is:{highest_stock_value}")
    print(f"Item with highest stock value:-{item_with_highest_stock_value}")





