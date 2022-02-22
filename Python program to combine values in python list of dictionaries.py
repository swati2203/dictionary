# Write a Python program to combine values in python list of dictionaries.
a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1','amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
i=0
b=[]
for i in a:
    for y in i.values():
        if y not in b:
            b.append(y)
print(b)