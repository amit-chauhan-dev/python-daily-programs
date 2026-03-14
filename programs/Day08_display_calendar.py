# – Display Calendar

import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

month_calendar = calendar.month(year, month)

print(month_calendar)