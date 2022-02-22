# Q41.Write a Python program to filter the height and width of students, which are stored in a
# dictionary.
# Original Dictionary:
student={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8,
66)}
s={}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}
for x,i in student.items():
    b=[]
    for j in i:
        b.append(j)
        height=b[0]
        weight=b[1]
        if height>6 and weight>70:
            s[x]=i
print(s)

