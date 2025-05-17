# Example file for Advanced Python: Hands On by Joe Marini
# Filter values out of a data set based on some criteria

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the filter() function gives us a way to remove unwanted data points
# TODO: create a subset of the data for days that had snowfall
snows = [day for day in weatherdata if day['snow'] > 0]
#pprint.pprint(snows)


snowdays = list(filter(lambda  x: x['snow'] > 0, weatherdata))
#pprint.pprint(snowdays)
#print(f'Snow days: {len(snowdays)}')


# filter can also be used on non-numerical data, like strings
# TODO: create a subset that contains summer days (july and Aug) with heavy rain (more than 1 in, about 2.5cm)
# def is_summer_rain_day(d):
#     summer_months = ['-07-', '-08-']
#     if d[4:8] in summer_months:
#         return True
#     else:
#         return False
# summer_rain = list(filter(lambda x:x['prcp'] >= 1.0 and is_summer_rain_day(x['date']),weatherdata))
# pprint.pp(summer_rain)
# print(len(summer_rain))

def is_summer_rain_day(d):
    summer_months = ['-07-', '-08-']
    if any([m in d['date'] for m in summer_months]) and d['prcp'] >= 1.0:
        return True
    return False

summer_rain = list(filter(is_summer_rain_day, weatherdata))

pprint.pp(summer_rain)
print(len(summer_rain))



