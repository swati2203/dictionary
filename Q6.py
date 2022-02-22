dic={
"ball":"red",
"bat":4,
"wickets":8,
"ball":"green",
"bat":3
}
b=[]
dic.pop("ball")
dic.pop("bat")
print(dic)
for i in dic.values():
    b.append(i)
print(b)


