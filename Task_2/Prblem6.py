''' Problem 6:
Generate a random password of 8 characters, including a mix of uppercase letters, lowercase letters, and numbers.
'''
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

characters = letters + numbers

password = ""
for i in range(8):
    password += random.choice(characters)

print(password)
