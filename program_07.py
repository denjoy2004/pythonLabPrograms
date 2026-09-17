word=input("Enter a word: ")
vowel="aeiouAEIOU"
vowels_list=[]
for each in word:
    if each in vowel:
        vowels_list.append(each)
print("Vowels in words are : ", vowels_list)