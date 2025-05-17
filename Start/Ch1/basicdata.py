# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
#my attempt
maxtemp = None
for d in weatherdata:
    if maxtemp:
        temp = d['tmax']
        if temp > maxtemp:
            maxtemp = temp
            day = d['date']
    else:
        maxtemp = d['tmax']
        day = d['date']
#print(f'I say the warmest day was {maxtemp} degrees on {day}')
 
#using max function
warmday = max(weatherdata, key=lambda x: x['tmax'])  #The lambda function is called over and over for each loop of weatherdata
#print(f'The warmest was was {warmday['tmax']} on {warmday['date']}')
# TODO: What was the coldest day in the data set?

coldday = min(weatherdata, key=lambda x: x['tmin'])
#print(f'The coolest was was {coldday['tmin']} on {coldday['date']}')

# TODO: How many days had snowfall?
count = 0
for d in weatherdata:
    if d['snow'] > 0.0:
        count += 1
#print(count)

#do the same with list comprehension
x = 0
snow_days = [i for i in weatherdata if i['snow'] > 0.0]  #creates a list []
print(f'Snow days: {len(snow_days)}')
pprint.pp(snow_days)