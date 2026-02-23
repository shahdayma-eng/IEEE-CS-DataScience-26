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

