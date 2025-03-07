def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def days_in_month(year, month):
	# Create a list with all months
	months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	# Check if month is valid
	if month < 1 or month > 12:
		# If not valid
		return None
	# Get the days for each month
	days = months[month - 1]
	# Check for leap year's February
	if month == 2 and is_year_leap(year):
		days = 29
	return days

def day_of_year(year, month, day):
    if year < 1582:
        return None
    if month < 1 or month > 12:
        return None
    if day < 1 or day > days_in_month(year, month):
        return None
    total_days = 0
    for m in range(1, month):
        total_days = total_days + days_in_month(year, m)
    total_days = total_days + day
    return total_days

print(day_of_year(2000, 12, 31))
