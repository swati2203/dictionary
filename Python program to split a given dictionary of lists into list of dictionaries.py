# # .Write a Python program to split a given dictionary of lists into list of dictionaries.
# # Original dictionary of list
marks={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# # Split said dictionary of lists into list of dictionaries:[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language':
# # 84}, {'Science': 95, 'Language': 80}]
# b=[]
# for i,j in marks.items():
#     b.append(i)
# print(b)
res = [{key : value[i] for key, value in marks.items()}
         for i in range(4)]
  
# printing result
print ("The converted list of dictionaries " +  str(res))


