#Apollo: grat tool to get in easy way weather forecast

#module
import sys
import json
import pyowm
# ----------------------function----------------------
def forecast(city,condition):
    #Default action
    #owm_ru = owm(language='it') # set default language to it
    # open config.json file(read)
    with open("config.json", "r") as data_file:
        data = json.load(data_file)
        owm = pyowm.OWM = (data["Api_Key"])
        Name = data["Name"]
        Surname = data["Surname"]
        if condition == True:
            city = data["City"]
        # close json
        data_file.close()
    #get weather forecast
    observation = owm.weather_at_place(city)
    weather = observation.get_weather()
    print(weather)
# ----------------------main----------------------
if len(sys.argv) == 1:
    print("\nWelcome to Apollo: The great weather forecast tool\n\n")
    check_default_city = True
    forecast('',check_default_city)
else:
    check_default_city = False
    #call forecast with user's city
    forecast(sys.argv[1],check_default_city)
