# Write a Python program to create a key-value list pairings in a given dictionary.
# Original dictionary:
a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachar Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]

c={}
b=[]
for i,j in a.items():
    for x in j:
        c[i]=x
b.append(c)
print(b)