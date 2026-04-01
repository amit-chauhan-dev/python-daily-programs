## Problem
Write a Python program to check whether a given year is a leap year or not.

## Program Description
This Python program takes a year as input from the user and determines whether it is a leap year based on standard rules.

## Leap Year Rules

- A year is a leap year if it is divisible by 400  
OR  
- A year is divisible by 4 but not divisible by 100  

## Logic Used

If (year % 400 == 0) OR (year % 4 == 0 AND year % 100 != 0) → Leap Year  
Else → Not a Leap Year  

## Concepts Used

- Python input()
- Integer data type
- Modulus operator (%)
- Logical operators (and, or)
- Conditional statements (if-else)