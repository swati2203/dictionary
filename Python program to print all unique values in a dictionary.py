# Write a Python program to print all unique values in a dictionary.
Data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
s=set()
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

for i in Data:
    for x in i.values():
        if x not in s:
            s.add(x)
print(s)
