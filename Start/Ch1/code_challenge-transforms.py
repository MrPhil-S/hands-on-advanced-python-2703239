#TASK: : Transform the entire list of each data record from being a dictionary object with keys and values into
#  a list of tuples with two items: the date of the data record and a string describing the average temperature
#  of the day as "cold," "warm," or "hot" based upon these rules:

import json
from pprint import pprint

def process(d): 
    avg_temp = lambda t1, t2: (t1 + t2)/2.0
    a = avg_temp(d['tmin'],d['tmax'])
    descr = ''
    if a <= 60:
        descr = 'cold'
    elif a > 60 and a < 80:
        descr = 'warm'
    elif a >= 80:
        descr = 'hot'
    return (d['date'], descr)

def get_day_temp_descriptions():
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)
    return list(map(process, weatherdata))


pprint(get_day_temp_descriptions())