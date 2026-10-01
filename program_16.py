n=int(input("Enter a number: "))
factor=1
for i in range(1,n):
    if(n%i==0):
        print("Factors are : ",i)