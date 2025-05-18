# Example file for Advanced Python: Hands On by Joe Marini
# Using the reduce function

import json
from functools import reduce

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: how much snowfall is in the entire dataset?
snowfall = reduce(lambda acc, x: acc + x['snow'], weatherdata, 0 )
print(snowfall)

#or more simply:
total_snow = sum(record.get('snow', 0) for record in weatherdata)
print(total_snow)

# TODO: how much total precipitation (rain AND snow) is in the entire dataset?
precipitation = reduce(lambda acc, x: acc + (x['snow'] + x['prcp']), weatherdata, 0 )
print(precipitation)

# TODO: What was the warmest day in which it snowed? Need to find highest 'tmax' for all
# days where 'snow' > 0
def warm_snow_day(acc, elem):
    # return the elem value if the snow amount > 0 and its tmax value is
    # larger than the tmax value that is in the acc argument
    return elem if elem['snow'] > 0 and elem['tmax'] > acc['tmax'] else acc

# define a "zero" value start date for the reduce function to start with
start_val = {
    "date": "1900-01-01",
    "tmin": 0,
    "tmax": 0,
    "prcp": 0.0,
    "snow": 0.0,
    "snwd": 0.0,
    "awnd": 0.0
}

# TODO: reduce the data set to the warmest snow day
result = reduce(warm_snow_day, weatherdata, start_val)
print(f'{result['date']} with temp of {result['tmax']} and snowfall as {result['snow']}')