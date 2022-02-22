


dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for i,j in dic1.items():
    for x,y in dic2.items():
        if x==i:
            dic1[i]=y+j
        else:
            dic1[x]=y
print(dic1)
