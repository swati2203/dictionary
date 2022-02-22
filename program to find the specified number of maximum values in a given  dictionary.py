# Python program to find the specified number of maximum values in a given
# dictionary.
d={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']
lst=[]
for i in d.values():
    lst.append(i)
i=0
while i<len(lst):
    j=0
    while j<len(lst)-i-1:
        if lst[j]<lst[j+1]:
            t=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=t
        j=j+1
    i=i+1
print(lst)
c=[]
max=int(input("enter the the no.of maximum you want"))
i=0
while i<=max:
    for x,y in d.items():
        if y==lst[i] and x not in c:
            c.append(x)
    i=i+1
print(c)

