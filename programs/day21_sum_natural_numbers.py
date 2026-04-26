# – Sum of Natural Numbers

'''Natural numbers are a set of positive integers that are used to count and order objects.
They are the numbers that typically start from 1 and continue indefinitely, including all the
whole numbers greater than 0. In mathematical notation, the set of natural numbers is often
denoted as "N" and can be expressed as.
N = 1,2,3,4,5,6,7,8,...
'''

limit = int(input("Enter the limit: "))

# check for valid input
if limit < 1:
    print("Please enter a positive integer")

else:
    total_sum = 0

# calculate sum
for i in range(1, limit + 1):
    total_sum += i

print(f"The sum of natural numbers up to {limit} is: {total_sum}")
