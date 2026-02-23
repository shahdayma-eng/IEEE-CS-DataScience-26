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

