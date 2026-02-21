<<<<<<< HEAD
filename = "Sample.txt"

with open(filename, 'r') as file:
    text = file.read()

words = text.split()

count = 0
for word in words:
    if len(word) > 5:
        count += 1

print(count)
=======
"""
Problem 7:
Write a program that takes a sentence and finds the longest word in it. 
Ex: Input: "Happiness can be found even in the darkest of times" 
      Output: The longest word is: Happiness

"""

s =input()

word= s.split() # to remove spaces
longest_word = max(word, key=len) #  اشوف مين الكبير باستخدام الكي
print("The longest word is:", longest_word)
>>>>>>> 930dcfc6675d349202124e8cc8ebb93a65d5f795
