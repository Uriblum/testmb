import pyowm
APIKEY='153776e15421d2c2e769848f351f1509'                  #your API Key here as string
OpenWMap=pyowm.OWM(APIKEY)                   # Use API key to get data
Weather=OpenWMap.weather_at_place('Tel-Aviv')  # give where you need to see the weather
Data=Weather.get_weather()                   # get out data in the mentioned location

temp = Data.get_temperature(unit='celsius')      # get current temparature in celsius
print ("Average Temp. Currently ", temp['temp']) # get avg. tmp
print ("Max Temp. Currently ", temp['temp_max']) # get max tmp
print ("Min Temp. Currently ", temp['temp_min']) # get min tmp>>
