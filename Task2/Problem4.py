<<<<<<< HEAD
n = int(input())
student_marks = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

query_name = input()

average = sum(student_marks[query_name]) / len(student_marks[query_name])
print("{:.2f}".format(average))
=======
'''
Problem 4:
Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) and print the result. 
Ex: Input: Num1: 10 || Num2: 5 || Operator: "/" 
       Output: 2.0
'''

num1= int(input("Num1:"))
num2= int(input("Num2:"))
operator =input("Operator:")
if operator== "+":
    res= num1 + num2
    print(res)
elif operator== "-":
    res= num1-num2
    print(res)

elif operator== "*":    # space = error
    res= num1*num2
    print(res)

elif operator== "/":
    res= num1/num2
    print(res)
>>>>>>> 930dcfc6675d349202124e8cc8ebb93a65d5f795
