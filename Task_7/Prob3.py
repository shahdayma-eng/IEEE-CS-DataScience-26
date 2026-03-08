import math

lam = float(input())
k = int(input())

ans = (math.exp(-lam) * (lam ** k)) / math.factorial(k)

print(f"{ans:.3f}")