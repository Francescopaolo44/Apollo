#Apollo: great tool to get weather forecast in easy way

#module
import sys
import json
from pyowm import OWM

# ----------------------class----------------------
class effect:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

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
    #get weather forecast and information about city
    observation = owm.weather_at_place(city)
    info = observation.get_weather()
    weather = info.get_detailed_status()
    wind = info.get_wind()
    temperature = info.get_temperature('celsius')
    humidity = info.get_humidity()
    #convert object to string
    weather_val = str(weather)
    wind_val = str(wind)
    temperature_val = str(temperature)
    humidity_val = str(humidity)
    #print information
    print("\n\n" + effect.BOLD + "Weather condition" + effect.END + "\n")
    print(effect.UNDERLINE + weather_val + effect.END)
    print("\n\n" + effect.BOLD + "Wind" + effect.END + "\n")
    print(wind_val)
    print("\n\n" + effect.BOLD + "Temperature [Celsius]" + effect.END + "\n")
    print(temperature_val)
    print("\n\n" + effect.BOLD + "Humidity" + effect.END + "\n")
    print(effect.UNDERLINE + humidity_val + "%" + "\n" + effect.END)

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
