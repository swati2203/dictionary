# Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
{'id': 2, 'success': False, 'name': 'Rabi'},
{'id': 3, 'success': True, 'name': 'Alex'}]
# Sample input if key is id: then 6
sum=0
for i in student:
    for x,y in i.items():
        if type(y)==int:
            sum+=y
print(sum)
