n=int(input("Enter the number of elements "))
list=[]
print("Enter element ")
for i in range(0,n):
    num=int(input())
    list.append(num)
print("The squares of the given numbers are : ")
for i in range(0,n):
    print(list[i]*list[i])