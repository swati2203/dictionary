# Write a Python program to convert a list into a nested dictionary of keys.
num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}
d=b={}
c={}
for i in num_list:
    b[i]={}
    b=b[i]
print(d)