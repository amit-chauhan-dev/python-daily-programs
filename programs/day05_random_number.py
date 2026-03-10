# – Random Number Generator

import random

print("Random Number Generator")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

random_number = random.randint(start, end)

print("Generated random number:", random_number)