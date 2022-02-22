# Q16.Write a Python program to map two lists into a dictionary.
key=[]
value=[]
n=int(input("enter the number of elements in dictionary"))
for i in range(n):
    name=input("enter the name")
    key.append(name)
for i in range(n):
    place=input("enter the city they live")
    value.append(place)
print(key)
print(value)
i=0
data={}
while i<len(key):
    data[(key[i])]=value[i]
    i=i+1
print(data)
