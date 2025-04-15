# OpenEDG Python Institute
# Python Essentials 2
# 4.6.1.13 LAB: the calendar module

import calendar  

class MyCalendar(calendar.Calendar):

    def count_weekday_in_year(self, year: int, weekday: int) -> int:
        """
        The weekday parameter should be a value between 0-6,
        where 0 is Monday and 6 is Sunday.
        The method should return the number of days as an integer.
        """
        counter = 0
        for month in range(1, 13):
            for day in self.itermonthdays2(year, month):
                if day[1] == weekday and day[0] != 0:
                    counter += 1
        return counter

# Example usage
my_cal = MyCalendar()

# Test case 1: 2019, weekday=0 (Monday)
print(my_cal.count_weekday_in_year(2019, 0))  # Should print 52

# Test case 2: 2000, weekday=6 (Sunday)
print(my_cal.count_weekday_in_year(2000, 6))  # Should print 53