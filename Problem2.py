'''
Problem 2:
Write a program that takes a temperature in Celsius and converts it to Fahrenheit using the formula: f = (c + 9/5)+32
Ex: Input: 37 
      Output: 37°C is equal to 98.6°F
'''

num=input()
f=(((int(num)+9/5)+32)) # it should be like this to calculate the right number f=(c*9/5)+32
print(f"{num}°C is equal to {f}°F")