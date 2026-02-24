# Check if data is valid
def check(d):
    if not isinstance(d, list):
        raise TypeError("Input must be a list.")

    if len(d) == 0:
        raise ValueError("List cannot be empty.")

    for x in d:
        if not isinstance(x, (int, float)):
            raise ValueError("All values must be numbers.")


#  Count elements
def count(d):
    c = 0
    for _ in d:
        c += 1
    return c


#  Add numbers manually
def total(d):
    t = 0
    for x in d:
        t += x
    return t


# Mean (average)
def mean(d):
    return total(d) / count(d)


#  Minimum value
def minimum(d):
    m = d[0]
    for x in d:
        if x < m:
            m = x
    return m


#  Maximum value
def maximum(d):
    m = d[0]
    for x in d:
        if x > m:
            m = x
    return m


#  Bubble Sort
def sort_list(d):
    s = d[:]   
    n = count(s)

    for i in range(n):
        for j in range(0, n - i - 1):
            if s[j] > s[j + 1]:
                temp = s[j]
                s[j] = s[j + 1]
                s[j + 1] = temp
    return s


#  Median
def median(d):
    s = sort_list(d)
    n = count(s)

    if n % 2 == 1:      # odd
        return s[n // 2]
    else:               # even
        a = s[(n // 2) - 1]
        b = s[n // 2]
        return (a + b) / 2


#  Quartiles
def quartiles(d):
    s = sort_list(d)
    n = count(s)

    mid = median(s)

    if n % 2 == 0:
        low = s[:n // 2]
        high = s[n // 2:]
    else:
        low = s[:n // 2]
        high = s[n // 2 + 1:]

    q1 = median(low)
    q3 = median(high)

    return q1, mid, q3


# Variance (population)
def variance(d):
    m = mean(d)
    n = count(d)

    v = 0
    for x in d:
        diff = x - m
        v += diff * diff

    return v / n


# Detect spikes (outliers)
def spikes(d):
    q1, mid, q3 = quartiles(d)
    iqr = q3 - q1
    limit = q3 + 1.5 * iqr

    s = []
    for x in d:
        if x > limit:
            s.append(x)

    return s