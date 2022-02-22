my_dict = {
    'a':50,
    'b':58,
    'c': 56,
    'd':40,
    'e':100,
    'f':20
}
max=0
a1=""
secmax=0
b1=""
thirmax=0
d1=""
for x,y in my_dict.items():
    if max<y:
        max=y
        c1=x
for x,y in my_dict.items():
    if y!=max and y>secmax:
        secmax=y
        b1=x
for x,y in my_dict.items():
    if y!=max and y!=secmax and y>thirmax:
        thirmax=y
        d1=x
print([c1,b1,d1])