# – LCM (Least Common Multiple)
'''
LCM, or Least Common Multiple, is the smallest multiple that is exactly divisible by two or
more numbers.
'''

# Python Program to find the L.C.M. of two input number
def compute_lcm(x, y):
    if x > y:           # choose the greater number
        greater = x
    else:
        greater = y
    while True :
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater 
            break
        greater += 1
    return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"The L.C.M. of {num1} and {num2} is {compute_lcm(num1, num2)} ")