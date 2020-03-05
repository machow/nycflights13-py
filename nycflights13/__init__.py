import pandas
from pkg_resources import resource_filename as _rf

flights = pandas.read_csv(_rf("nycflights13", "data/flights.csv.zip"))
airlines = pandas.read_csv(_rf("nycflights13", "data/airlines.csv"))
planes   = pandas.read_csv(_rf("nycflights13", "data/planes.csv"))
weather  = pandas.read_csv(_rf("nycflights13", "data/weather.csv"))
airports = pandas.read_csv(_rf("nycflights13", "data/airports.csv"))

