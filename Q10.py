dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
for x in dict1.values():
    for i in x:
        count+=1
print(count)