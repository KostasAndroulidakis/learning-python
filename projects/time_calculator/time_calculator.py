# ==============freeCodeCamp==============>
# ====Scientific Computing with Python====>
# ====Build a Time Calculator Project=====>

def add_time(start, duration, day_of_week=None):
    # Constants
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    
    # Parse start time
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))
    
    # Convert to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0
    
    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Calculate total minutes
    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // MINUTES_PER_HOUR
    final_minutes = total_minutes % MINUTES_PER_HOUR
    
    # Calculate total hours and days
    total_hours = start_hour + duration_hour + extra_hours
    days_passed = total_hours // HOURS_PER_DAY
    final_hours = total_hours % HOURS_PER_DAY
    
    # Now we need to convert back to 12-hour format
    if final_hours == 0:
        final_hours = 12
        period = 'AM'
    elif final_hours == 12:
        period = 'PM'
    elif final_hours >= 13:
        final_hours = final_hours - 12
        period = 'PM'
    else:
        period = 'AM'

    # And format the result with day of week and days later
    days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Handle day of week (if provided)
    day_part = ""
    if day_of_week is not None:
        days_of_the_week = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
        # Make it case insensitive
        day_of_week = day_of_week.capitalize()
        # Find the index of the day
        day_index = days_of_the_week.index(day_of_week)
        # Calculate new day index
        new_day_index = (day_index + days_passed) % 7
        # Get the new day name
        new_day = days_of_the_week[new_day_index]
        day_part = f", {new_day}"

    # Handle the "days later" part
    days_later_text = ""
    if days_passed == 1:
        days_later_text = " (next day)"
    elif days_passed > 1:
        days_later_text = f" ({days_passed} days later)"

    # Format the time string
    formatted_time = f"{final_hours}:{final_minutes:02d} {period}"

    # Combine time with day of week (if provided) and days later text
    new_time = formatted_time + day_part + days_later_text

    # Return the final result
    return new_time
