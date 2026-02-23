
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

