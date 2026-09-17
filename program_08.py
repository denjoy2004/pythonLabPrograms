from itertools import count

s=input("Enter a string ")
key=input("Enter the word to be searched ")
sr=s.split(" ")
count=0
for each in sr:
    if each==key:
        count+=1
print("The word ",key," appears ",count,"times" )