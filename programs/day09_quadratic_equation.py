# – Quadratic Equation Solver
import math

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Check if 'a' is zero
if a == 0:
    print("This is not a quadratic equation because a = 0.")
else:
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check the nature of the roots
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")

    elif discriminant == 0:
        # One real root
        root = -b / (2*a)
        print(f"Root: {root}")

    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)

        print(f"Root 1: {real_part} + {imaginary_part}i")
        print(f"Root 2: {real_part} - {imaginary_part}i")