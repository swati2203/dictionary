my_dict = {
    'a':50,
    'b':58,
    'c':56,
    'd':40,
    'e':100,
    'f':20
}

max=0
secmax=0
thirmax=0
for x in my_dict.values():
    if x>max:
        max=x
for x in my_dict.values():
    if x!=max and x>secmax:
        secmax=x
for x in my_dict.values():
    if x!=max and x!=secmax and x>thirmax:
        thirmax=x
print([thirmax,secmax,max])