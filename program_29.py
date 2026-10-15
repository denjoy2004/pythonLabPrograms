num1=[]
num2=[]
n1=int(input("Enter the limit of the first list : "))
for i in range (0,n1):
    n=int(input())
    num1.append(n)

n2=int(input("Enter the limit of the second list : "))
for i in range (0,n2):
    n=int(input())
    num2.append(n)

print("List 1 : ",num1)
print("List 2 : ",num2)
if(len(num1)==len(num2)):
    print("Length of the both list is same, Lenght = ",len(num1))
else:
    print("Lengh of the both list is not same")
sum1=0
sum2=0
for i in num1:
    sum1+=i

for i in num2:
    sum2+=i
if sum1==sum2:
    print("sum of integeres in list 1 and list 2 is equal : ",sum1)
else:
    print("sum of integeres in list 1 and list 2 is not equal\nList 1 = ",sum1,"\nList 2 = ",sum2)

common=[]
for  a in num1 :
    if a in num2 and a not in common:
        common.append(a)

if common:
    print("The common element in list 1 and list 2 is ",common)
else:
    print("There is no common element in list 1 and list 2 is ")


