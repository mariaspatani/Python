"""
Author:Maria
Date:22/11/2024
Version:1.1
This is a python to find the index of a minimum value in a tuple.
"""
tuple1=(5,6,2,8,9,6,1,3,7)
min(tuple1)
print("Min Value:",min(tuple1))
#convet tuple into list
list1=list(tuple1)
print(list1)
list1.index(min(list1))
print("The index  of the least number from the list:",list1.index(min(list1)))
tuple2=tuple(list1)
print("The index  of the least number from the tuple:",tuple2.index(min(tuple2)))





