# Write a Python program to print a dictionary in table format.
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# Sample Output:
# C1 C2 C3
# 159
# 2 6 10
# 3 7 11
for i in my_dict.keys():
    print(i,end=" ")
for x in my_dict.values():
    i=0
    while i<len(x):
        print()
        print(x[i],end=' ')
        for y in my_dict.values():
            if y!=x:
                print(y[i],end=" ")
        i=i+1