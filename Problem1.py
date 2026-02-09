'''
Problem 1:
Write a program that takes the user's name and birth year as input, then calculates and prints their current age. 
Ex: Input: Name: Sohaila || Birth Year: 2004 
      Output: "Hello Sohaila, you are 22 years old."
'''

name =input("Name: ")
year=input("Birth year: ")
age = 2026 - int(year) # i used int()because year is string so must cconvert it to integer
print(f"Hello {name}, you are {age} years old")