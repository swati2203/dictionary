# Write a Python program to match key values in two dictionaries.
dict1={'key1': 1, 'key2': 3, 'key3': 2}
dict2={'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
for i,j in dict1.items():
    for x,y in dict2.items():
        if i==x and j==y:
            print(i,":",j,"is present in dict1 and dict2")