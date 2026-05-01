# Highest Common Factor(HCF):
'''
HCF, or Highest Common Factor, is the largest positive integer that divides two or more
numbers without leaving a remainder.
'''

#  Python program to find H.C.F of two numbers

def compute_hcf(x, y):

    # choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    
    hcf = 1 # initialize

    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"The HCF of {num1} and {num2} is {compute_hcf(num1, num2)}")