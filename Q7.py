lst=[
    {"first":"1"}, 
    {"second": "2"}, 
    {"third": "1"},
    {"four": "5"},
    {"five":"5"},
    {"six":"9"},
    {"seven":"7"}
]
b=[]
for i in lst:
    for j in i.values():
        if j not in b:
            b.append(j)
print(b)