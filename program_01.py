n1=int(input("Enter the 1st number:"))
n2=int(input("Enter the 2nd number:"))
n3=int(input("Enter the 3rd number:"))
if(n2>=n1 and n2>=n3):
    largest=n2
else:
    largest=n3
print("The largest number is ",largest)
