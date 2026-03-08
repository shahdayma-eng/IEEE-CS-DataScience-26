import math

p_percent, n = map(float, input().split())

n = int(n)

p = p_percent / 100

# P(X <= 2)
prob_no_more_than_2 = sum(
    math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    for k in range(0, 3)
)

# P(X >= 2)
prob_at_least_2 = 1 - sum(
    math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    for k in range(0, 2)
)

print(f"{prob_no_more_than_2:.3f}")
print(f"{prob_at_least_2:.3f}")