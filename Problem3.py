'''
Problem 3:
Write a Python program that takes a string as input and counts how many vowels (a, e, i, o, u) it contains. 
Ex: Input: "Data Science" 
      Output: The number of vowels is: 5

'''

word=input()
vowels = "aeiouAEIOU"
cnt=0
for i in word :
    if i in vowels :
        cnt+=1

print(f"The number of vowels is: {cnt}")