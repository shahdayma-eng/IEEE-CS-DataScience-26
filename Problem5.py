'''
Problem 5: 
Write a program that takes a positive integer n and prints the first n numbers of the Fibonacci sequence. 
Ex: Input: 5 
      Output: 0, 1, 1, 2, 3

'''
num=int(input())
a=0
b=1           # الرقم الي احنا واقفين عنده يساوي مجموع الرقمين الي قبله
c=0
for i in range(num):
    print(c)
    a=b
    b=c 
    c=a+b