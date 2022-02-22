dictA = {'Sun': 5, 'Mon': 3, 'Tue': 5, 'Wed': 3}
c={}
for x,y in dictA.items():
    if y not in c:
        c[y]=[x]
    else:
        c[y].append(x)
print(c)
