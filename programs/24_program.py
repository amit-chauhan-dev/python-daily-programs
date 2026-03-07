#  Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.

'''Converting a decimal number to binary, octal, and hexadecimal involves dividing the
decimal number by the base repeatedly and noting the remainders at each step. Here's a
simple example:
'''

# 1. Binary:
'''
    Divide 27 by 2. Quotient is 13, remainder is 1. Note the remainder.
    Divide 13 by 2. Quotient is 6, remainder is 1. Note the remainder.
    Divide 6 by 2. Quotient is 3, remainder is 0. Note the remainder.
    Divide 3 by 2. Quotient is 1, remainder is 1. Note the remainder.
    Divide 1 by 2. Quotient is 0, remainder is 1. Note the remainder.
'''

# 2.Octal:
'''
    Divide 27 by 8. Quotient is 3, remainder is 3. Note the remainder.
    Divide 3 by 8. Quotient is 0, remainder is 3. Note the remainder.
'''

# 3. Hexadecimal:
'''
    Divide 27 by 16. Quotient is 1, remainder is 11 (B in hexadecimal). Note the
    remainder.
'''

dec_num = int(input('Enter a decimal number: '))

print("the decimal value of", dec_num, "is:")
print(bin(dec_num), "in binary.")
print(oct(dec_num), "in octal.")
print(hex(dec_num), "in hexadecimal.")