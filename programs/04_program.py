#  Write a Python program to swap two variables.

# input two variable 
a = input("Enter the value of the firt variable (a):  ")
b = input("Enter the value of the second variable (b):  ")
# display the original values
print(f"original value : a = {a}, b = {b}")
# swap the value using a temporary variable
temp = a
a = b
b = temp
print(f"swapd value: a = {a}, b = {b}")