# Write a Python Program to Find Armstrong Number in an Interval.

# input the interval from the user 
lower = int(input("Enter the lower limit of the interval:"))
upper = int(input("Enter the upper limit of the interval:"))

for num in range(lower , upper + 1):  #iterate through the numbers i
    order = len(str(num))  #finde the number of digit in 'num'
    temp_num = num 
    sum = 0

    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** order 
        temp_num //= 10

    # check if 'num' is an armstrong number 
    if num == sum:
        print(num)