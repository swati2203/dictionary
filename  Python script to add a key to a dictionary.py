# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

dic={0:10,1:20}
n=int(input("enter the number of keys you want to add"))
for i in range(n+1):
    x=int(input("enter the key"))
    y=int(input("enter the values"))
    dic[x]=y
print(dic)