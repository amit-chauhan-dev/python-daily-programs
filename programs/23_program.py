# Write a Python Program to Find HCF. 

'''
    HCF, or Highest Common Factor, is the largest positive integer that divides two or more
    numbers without leaving a remainder.
 '''

#   python program to find H.C.F of two numbers

#define a function
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
        return hcf 

num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number'))