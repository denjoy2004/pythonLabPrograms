n=int(input("Enter the limit of the list "))
numbers=[]
print("Enter the list")
for i in range(0,n):
    element=int(input())
    numbers.append(element)
print("Positive numbers are ")
for i in range(0,n):
    if numbers[i]>0:
        print(numbers[i])
