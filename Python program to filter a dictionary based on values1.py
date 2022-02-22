# write a Python program to convert more than one list to nested dictionary.
# Original strings:
x=['S001', 'S002', 'S003', 'S004']
y=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
z=[85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}},
# {'S004': {'Saim Richards': 92}}]

i=0
b=[]
while i<len(x):
    a={}
    c={}
    a[y[i]]=z[i]
    c[x[i]]=a
    b.append(c)
    i=i+1
print(b)
