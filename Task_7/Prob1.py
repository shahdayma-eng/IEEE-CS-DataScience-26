ratio, n = map(float, input().split())

n = int(n)

p = ratio / (1 + ratio)

ans = 1 - (1 - p) ** n

print(f"{ans:.3f}")