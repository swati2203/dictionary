# Write a Python program to drop empty Items from a given Dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

dic={'c1':'Red','c2':'Green','c3':None}
dic2={}
for i,j in dic.items():
    if j!=None:
        dic2[i]=j
print(dic2)