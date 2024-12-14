# Define constants
METERS_PER_MILE = 1609.344
LITERS_PER_GALLON = 3.785411784
DISTANCE_IN_MILES = 100000 / METERS_PER_MILE
KILOMETERS_PER_MILE = METERS_PER_MILE / 1000

def liters_100km_to_miles_gallon(liters):   
    # Convert liters to gallons
    gallons = liters / LITERS_PER_GALLON
    # Get Miles per Gallon
    miles_per_gallon = DISTANCE_IN_MILES * (1 / gallons)
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    # Convert miles to kilometers
    kilometers = miles * KILOMETERS_PER_MILE
    # Get liters per 100km
    liters_per_100km = (100 * LITERS_PER_GALLON) / kilometers
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
