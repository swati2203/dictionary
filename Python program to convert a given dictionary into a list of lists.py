# Write a Python program to convert a given dictionary into a list of lists.
# Original Dictionary:
color={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
b=[]
for i,j in color.items():
    b.append([i,j])
print(b)