import math

mu, sigma = map(float, input().split())

x = float(input())

a, b = map(float, input().split())

def normal_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

# P(X < x)
prob1 = normal_cdf((x - mu) / sigma)

# P(a < X < b)
prob2 = normal_cdf((b - mu) / sigma) - normal_cdf((a - mu) / sigma)

print(f"{prob1:.3f}")
print(f"{prob2:.3f}")