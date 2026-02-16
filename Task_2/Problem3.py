<<<<<<< HEAD
students = []

n = int(input())

for _ in range(n):  #--> _ means that we dont want to knoe it postion we just want it repeat n of times
    name = input()
    grade = float(input())
    students.append([name, grade])

grades = sorted(set(student[1] for student in students)) # the deffreence between sort()and sorted() is sort()we use it only with lists 

second_lowest = grades[1]

names = [student[0] for student in students if student[1] == second_lowest]

names.sort()

for name in names:
    print(name)
=======
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
>>>>>>> 930dcfc6675d349202124e8cc8ebb93a65d5f795
