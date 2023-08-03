import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)
year = 2023
month = 8
cal_str = cal.formatmonth(year, month)
print(cal_str)
