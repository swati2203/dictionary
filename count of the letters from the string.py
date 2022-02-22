# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
str='w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
str_dic={}
for i in str:
    count=0
    for j in str:
        if i==j:
            count+=1
        str_dic[i]=count
print(str_dic)
