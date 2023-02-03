import calendar
print("Full calendar")
print(calendar.calendar(2023))
print("particular month")
print(calendar.month(2023,1))
print("set first day of week")
calendar.setfirstweekday(calendar.WEDNESDAY)
print(calendar.month(2023,1))

