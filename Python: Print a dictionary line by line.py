# Python: Print a dictionary line by line
students = {'Aex':{'class':'V',
'rolld_id':2},
'Puja':{'class':'V',
'roll_id':3}}
# Sample Output:
# Aex
# class : V
# rolld_id : 2Puja
# class : V
# roll_id : 3
for i,j in students.items():
    print(i)
    for x,y in j.items():
        print(x,":",y)