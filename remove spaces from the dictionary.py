Product_list = {'P 01' : 'DBMS', 'P 02' : 'OS',
                'P 0 3 ': 'Soft Computing'}
Product_list2={}
for i,y in Product_list.items():
    key2=""
    for j in i:
        if j!=" ":
            key2+=j
    Product_list2[key2]=y
print(Product_list2)