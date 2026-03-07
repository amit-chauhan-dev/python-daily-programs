#  Write a Python program to display calendar.

import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

terminet = calendar.month(year, month)
print(terminet)