<<<<<<< HEAD
n = int(input())  # video number 21
a_lst = []    # the word list is a built in 
for i in range(n):
    command = input().split()

    if command[0] == "insert":
        index = int(command[1])
        value = int(command[2])
        a_lst.insert(index, value)

    elif command[0] == "print":
        print(a_lst)

    elif command[0] == "remove":
        value = int(command[1])
        a_lst.remove(value)

    elif command[0] == "append":
        value = int(command[1])
        a_lst.append(value)

    elif command[0] == "sort":
        a_lst.sort()

    elif command[0] == "pop":
        a_lst.pop()

    elif command[0] == "reverse":
        a_lst.reverse()
=======
'''
Problem 2:
Write a program that takes a temperature in Celsius and converts it to Fahrenheit using the formula: f = (c + 9/5)+32
Ex: Input: 37 
      Output: 37°C is equal to 98.6°F
'''

num=input()
f=(((int(num)+9/5)+32)) # it should be like this to calculate the right number f=(c*9/5)+32
print(f"{num}°C is equal to {f}°F")
>>>>>>> 930dcfc6675d349202124e8cc8ebb93a65d5f795
