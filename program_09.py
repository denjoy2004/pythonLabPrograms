n=int(input("Enter the number of elements: "))
numbers=[]
print("Enter the elements ")
for i in range(0,n):
    element=int(input())
    if(element>100):
        numbers.append('over')
    else:
        numbers.append(element)
print(numbers)