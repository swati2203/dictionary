# Q15.Write a Python program to remove a key from a dictionary.
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
n=input("enter the key you want to remove")
if n in test_dict:
    test_dict.pop(n)
else:
    print("not present in dictionary")
print(test_dict)