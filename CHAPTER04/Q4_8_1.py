import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)
year = 2023
month = 8
cal_str = cal.formatmonth(year, month)
cal_str = cal_str.replace("Su", "\033[31mSu\033[0m")
cal_str = cal_str.replace("Sa", "\033[34mSa\033[0m")


print(cal_str)
