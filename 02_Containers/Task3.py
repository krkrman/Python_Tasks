import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

print("Calendar for", calendar.month_name[month], year)
print(calendar.month(year, month))
