c={'bijender':45,'deepak':60,'param':20,'anjali':30,'roshini':50}
b=[]
for i in c.values():
    b.append(i)
i=0
# acending order dictionary
while i<len(b):
    j=0
    while j<(len(b)-i-1):
        if b[j]>b[j+1]:
            t=b[j]
            b[j]=b[j+1]
            b[j+1]=t
        j=j+1
    i=i+1
print(b)
Adic={}
for i in b:
    for x,y in c.items():
        if y==i:
            Adic[x]=i
print(Adic)
# descending order dictionary
# i=0
# while i<len(b):
#     j=0
#     while j<(len(b)-i-1):
#         if b[j]<b[j+1]:
#             t=b[j]
#             b[j]=b[j+1]
#             b[j+1]=t
#         j=j+1
#     i=i+1
# Ddic={}
# for i in b:
#     for x,y in c.items():
#         if y==i:
#             Ddic[x]=i
# print(Ddic)
    
