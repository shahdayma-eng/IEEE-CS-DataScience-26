<<<<<<< HEAD
import math

def vector_sub(a, b):
    return [a[i] - b[i] for i in range(3)]

def cross_product(u, v):
    return [u[1]*v[2] - u[2]*v[1],
            u[2]*v[0] - u[0]*v[2],
            u[0]*v[1] - u[1]*v[0]]

def dot_product(u, v):
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

def magnitude(v):
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def angle_between_planes(P, Q, R, S):
    PQ = vector_sub(Q, P)
    PR = vector_sub(R, P)
    PS = vector_sub(S, P)

    n1 = cross_product(PQ, PR)
    n2 = cross_product(PS, PR)

    cos_theta = dot_product(n1, n2) / (magnitude(n1) * magnitude(n2))
    theta = math.degrees(math.acos(cos_theta))
    return theta

P = list(map(float, input().split()))
Q = list(map(float, input().split()))
R = list(map(float, input().split()))
S = list(map(float, input().split()))

theta = angle_between_planes(P, Q, R, S)
print("{:.2f}".format(theta))
=======
"""
Problem 8:
Write a program that takes the coordinates of two points (x1, y1) and (x2, y2) and calculates the Euclidean distance between them using the math library. Formula: d = (x2-x1)2+(y2-y1)2
Ex:Input: P1(0,0) || P2(3,4)
     Output: The distance is: 5.0
"""

import math
x1=int(input("x1 ="))
y1=int(input("y1 ="))
x2=int(input("x2 ="))
y2=int(input("y2 ="))
d=math.sqrt((x2-x1)**2 +(y2-y1)**2)
print(f"The distance is:{d} ")
>>>>>>> 930dcfc6675d349202124e8cc8ebb93a65d5f795
