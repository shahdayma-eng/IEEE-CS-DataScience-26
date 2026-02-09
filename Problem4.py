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
