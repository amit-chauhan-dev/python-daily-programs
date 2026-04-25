#  – Armstrong Numbers in an Interval

# Input the interval from the user
lower = int(input("Enter the lower limit of the interval: "))
upper = int(input("Enter the upper limit of the interval: "))

print("Armstrong numbers in the given interval are:")

for num in range(lower, upper + 1):  # Iterate through the numbers

    if num < 0:
        continue  # Skip negative numbers

    order = len(str(num))  # Number of digits
    temp_num = num
    sum_of_powers = 0

    while temp_num > 0:
        digit = temp_num % 10
        sum_of_powers += digit ** order
        temp_num //= 10

    # Check if Armstrong
    if num == sum_of_powers:
        print(num)