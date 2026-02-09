"""
Problem 9:
Write a program that takes a positive integer and checks if it is an Armstrong Number (a number that is equal to the sum of its own digits each raised to the power of the number of digits). 
Ex: Input: 153 
Output: 153 is an Armstrong number (13 + 53 + 33= 153)

"""
num=int(input())
old= num
total = 0
n = len(str(num)) 

while num > 0:
    digit= num % 10      
    total+= digit ** n    
    num =num // 10        #باخد الرقم الصحيح بس
    
if total == old:
    print(f"{old} is an Armstrong number")
else:
    print(f"{old}is not an Armstrong number")
