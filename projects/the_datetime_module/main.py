# OpenEDG Python Institute
# Python Essentials 2
# 4.5.1.22 LAB: The datetime and time modules

from datetime import datetime

dt_object = datetime(2020, 11, 4, 14, 53, 0)

print(dt_object.strftime('%Y/%m/%d %H:%M:%S'))         # Line 1: 2020/11/04 14:53:00
print(dt_object.strftime('%y/%B/%d %H:%M:%S PM'))      # Line 2: 20/November/04 14:53:00 PM
print(dt_object.strftime('%a, %Y %b %d'))              # Line 3: Wed, 2020 Nov 04
print(dt_object.strftime('%A, %Y %B %d'))              # Line 4: Wednesday, 2020 November 04
print(dt_object.strftime('Weekday: %w'))               # Line 5: Weekday: 3
print(dt_object.strftime('Day of the year: %j'))       # Line 6: Day of the year: 309
print(dt_object.strftime('Week number of the year: %U')) # Line 7: Week number of the year: 44