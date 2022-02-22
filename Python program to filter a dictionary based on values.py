# Write a Python program to filter a dictionary based on values.
a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
c={}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
for i,j in a.items():
    if j>170:
       c[i]=j
print(c) 