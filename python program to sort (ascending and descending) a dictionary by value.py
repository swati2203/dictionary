# Write a Python program to sort (ascending and descending) a dictionary by value.
dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value : [(0, 0), (2, 1), (1, 2), (4, 3), (3,
b=[]
for i in dic.values():
    b.append(i)
print(b)
l=len(b)
i=0
while i<l:
    j=0
    while j<(l-i-1):
        if b[j]>b[j+1]:
            t=b[j]
            b[j]=b[j+1]
            b[j+1]=t
        j=j+1
    i=i+1
print(b)
c=[]
for i in b:
    for x,y in dic.items():
        if y==i:
            c.append((x,i))
print(c)





