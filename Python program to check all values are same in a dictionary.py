# Write a Python program to check all values are same in a dictionary. Go to the editor
# Original Dictionary:
a={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
n=int(input("enter the number"))
count=0
count1=0
for i in a.values():
    count+=1
    if n==i:
        count1+=1
if count==count1:
    print("all the values contain",n)
