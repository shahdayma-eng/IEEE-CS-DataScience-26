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
