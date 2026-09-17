n=int(input("Enter the number of elemnts in the list "))
numbers=[]
print("Enter the elements ")
for i in range(0,n):
    num=int(input())
    numbers.append(num)
print("Original list is ",numbers)
replaced_list=[]
for i in range(0,n):
    if i%2!=0:
        replaced_list.append(i)
print("Replaced list is ",replaced_list)
