#  Write a Python Program to Find LCM.

#   Python program to find the L.C.M. of two input number 
def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater 
            break
        greater += 1
    return

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))

print("the L.C.M. is", compute_lcm(num1, num2))