# Q22. Write a Python program to create and display all combinations of letters, selecting each
# letter from a different key in a dictionary. Go to the editor
data={'1':['a','b'], '2':['c','d'],'3':['e','f'],'4':['g','h'],'5':['i','j'],'6':['k','l'],'7':['m','n'],
'8':['o','p'],'9':['q','r'],'10':['s','t'],'11':['u','v'],'12':['w','x'],'13':['y','z']}
a=[]
# Expected Output:
# ac
# ad
# bcbd
for i in data.values():
    j=0
    while j<len(i):
        for x in data.values():
            if x!=i:
                print(x[j]+i[j])
        j=j+1