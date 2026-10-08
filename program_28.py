names=input("Enter names seperated by space").split()
count=0
for name in names:
    count+=name.count('a')
print("Name : ",names)
print("Occurrences of 'a' : ",count)