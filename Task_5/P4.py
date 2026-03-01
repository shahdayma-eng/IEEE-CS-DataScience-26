import re

n = int(input())
for _ in range(n):
    s = input().strip()
    try:
        re.compile(s)
        print(True)
    except re.error:
        print(False)