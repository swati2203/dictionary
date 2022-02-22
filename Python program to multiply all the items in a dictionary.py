# Q14.Write a Python program to multiply all the items in a dictionary.
b={"a":30,"b":56,"c":9,"d":2,"e":10}
mul=1
for i in b.values():
    mul*=i
print(mul)
