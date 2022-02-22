# Write a Python program to remove a specified dictionary from a given list.
from ast import Break


a=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color':
'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color':
# 'Olive'}]
# b=input("enter the key remove")
z=input("enter the value also")
i=0
while i<len(a):
    if a[i]['id']==z:
        del a[i]
        break
print(a)