## Problem
Write a Python program to solve a quadratic equation.

A quadratic equation has the form:

ax² + bx + c = 0

## Program Description
This Python program calculates the roots of a quadratic equation using the quadratic formula.

The program:
1. Takes the coefficients `a`, `b`, and `c` as input from the user.
2. Calculates the discriminant.
3. Determines whether the equation has:
   - Two real and distinct roots
   - One real root
   - Two complex roots
4. Displays the calculated roots.

## Formula Used

Discriminant:

D = b² - 4ac

Roots:

x = (-b ± √D) / 2a

## Concepts Used

- Python input()
- Float data type
- Mathematical operations
- Conditional statements (`if`, `elif`, `else`)
- `math` module
- Square root using `math.sqrt()`