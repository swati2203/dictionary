# Q20.Write a Python program to check a dictionary is empty or not.
dic={2:{},3:{9:27},4:{}}
for i,j in dic.items():
    if j=={}:
        print(i,j)
