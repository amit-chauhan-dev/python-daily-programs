#  Write a Python program to solve quadratic equation.

import math

# input coefficients
a = float(input("Enter coefficients a:  "))
b = float(input("Enter coefficients b:  "))
c = float(input("Enter coefficients c:  "))

#calculate the disciriminent 
discriminant = b ** 2 - 4*a*c

#chek if the discrimenant is positive, negative, or zero 
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"ropt 1: {root1}")
    print(f"root 2: {root2}")
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    #  complex roots 
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")