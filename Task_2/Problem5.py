<<<<<<< HEAD
n = int(input())

for _ in range(n):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)
=======
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
>>>>>>> 930dcfc6675d349202124e8cc8ebb93a65d5f795
