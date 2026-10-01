dict={}
n=int(input("Enter the number of elememts : "))
for i in range(n):
    key = input("Enter key : ")
    value = input("Enter value : ")
    dict[key] = value
print("The dictionary is : ",dict)
dict_asc=sorted(dict.items())
print("Dictionary in ascending order : ",dict_asc)
dict_desc=sorted(dict.items(),reverse=True)
print("Dictionary in ascending order : ",dict_desc)
