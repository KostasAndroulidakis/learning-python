def is_year_leap(year):
      if year % 400 == 0:
        return True
      elif year % 100 == 0 and year % 400 != 0:
        return False
      elif year % 4 == 0:
        return True
      return False

# Create function
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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
