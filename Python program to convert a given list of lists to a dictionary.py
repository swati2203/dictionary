# Write a Python program to convert a given list of lists to a dictionary.
# Original list of lists:
d=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5,
'Zachary Simon', 'VII']]
# Convert the said list of lists to a dictionary:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5:
# ['Zachary Simon', 'VII']}
c={}
b=[]
for i in d:
    c[(i[0])]=i[1:]
print(c)

