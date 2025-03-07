hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

count_mins = mins + dura
count_hours = hour + count_mins // 60

hour_in_clock = count_hours % 24
mins_in_clock = count_mins % 60

print(hour_in_clock,mins_in_clock,sep=":")
