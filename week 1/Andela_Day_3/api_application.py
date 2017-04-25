
# my api c9012dd6fa863fea61c14f0e8c0ca5a8

# OpenWeatherMap API
# I start the code by importing the pyowm library that will get weather information.
import pyowm
# Next I create a variable called owm,
# used to shorten and contain my API key. This makes it easier to work with.

owm = pyowm.OWM('c9012dd6fa863fea61c14f0e8c0ca5a8')
# create another variable that will set the location that We wish to use for our weather query.
set_location = (owm.weather_at_place(input('Enter country or city whose climate details/data, You may want to know: ')))
# set_location = raw_input('enter some data: ')
# WE CALL OUR NEXT VARIABLE ,WE USE weather_value TO SHORTEN THE FUNCTION
# IT WILL HELP U GATHER YOU INFORMATION YUOR TRYING TO PULL.
weather_value = set_location.get_weather()
# WIND IS USED TO CAPTURE THE WIND SPEED AND DIRECTION.
wind = weather_value.get_wind()
# for the termperature
temperature = weather_value.get_temperature('celsius')
# for the Cloudiness
clouds = weather_value.get_clouds()

# Pressure
# Humidity

# PRINTING OUR CONTENTS
print(weather_value)
print(wind)
print(temperature)
print(clouds)
