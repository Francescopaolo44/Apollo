#Apollo: grat tool to get in easy way weather forecast

#module
import sys
import json
from pyowm import OWM
# ----------------------function----------------------
def forecast(city,condition):
    # open config.json file(read)
    with open("config.json", "r") as data_file:
        data = json.load(data_file)
        owm = OWM(data["Api_Key"])
        Name = data["Name"]
        Surname = data["Surname"]
        if condition == True:
            city = data["City"]
        # close json
        data_file.close()
    #get weather forecast and information
    observation = owm.weather_at_place(city)
    weather = observation.get_weather()
    print(weather)
# ----------------------main----------------------
if len(sys.argv) == 1:
    print("\nWelcome to Apollo: The great weather forecast tool\n\n")
    print("Weather forecast for default city are:\n\n")
    check_default_city = True
    forecast('',check_default_city)
else:
    check_default_city = False
    #call forecast with user's city
    forecast(sys.argv[1],check_default_city)
