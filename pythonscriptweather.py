import pyowm
APIKEY='153776e15421d2c2e769848f351f1509'       
OpenWMap=pyowm.OWM(APIKEY)                   
Weather=OpenWMap.weather_at_place('Tel-Aviv')  
Data=Weather.get_weather()                   

temp = Data.get_temperature(unit='celsius')      
print ("Average Temp. Currently ", temp['temp']) 
