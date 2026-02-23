
filename = "Sample.txt"

with open(filename, 'r') as file:
    text = file.read()

words = text.split()

count = 0
for word in words:
    if len(word) > 5:
        count += 1

print(count)

