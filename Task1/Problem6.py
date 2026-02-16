'''
Problem 6:
Write a program that takes a positive integer and prints its multiplication table from 1 to 10, but skips the result if it's a multiple of 4. 
Ex: Input: 3 
      Output: 3, 6, 9, 15, 18, 21, 27, 30 (Note: 12 and 24 are skipped)

'''
num=int(input())
for i in range(1,11):
    res=num*i
    
    if res %4==0:
         continue
    print(res)