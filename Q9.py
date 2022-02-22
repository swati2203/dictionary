str="MISSISSIPPI"
b=[]
for i in str:
    if i not in b:
        b.append(i)
c={}
for i in b:
    count=0
    for j in str:
        if i==j:
            count+=1
    c[i]=count
print(c)