# .Write a Python program to filter even numbers from a given dictionary values.
# Original Dictionary:
a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

for i,j in a.items():
    for x in j:
        if x%2!=0:
            j.remove(x)
print(a)