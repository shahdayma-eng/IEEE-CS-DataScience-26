
n = int(input())
scores = list(map(int, input().split()))

scores = list(set(scores))  # we do this to remove duplicates
scores.sort()

print(scores[-2])  

