class CurrentWeather:
        weather_data={'Toronto': ['13','partly sunny','8 km/h NW'],'Montreal':['16','mostly sunny','22 km/h W']}
        def __init__(self, city) : 
                self.city = city
        def getTemperature(self) :
                return self.weather_data [self.city][0]
        def getWeatherConditions(self) :
                return self.weather_data [self.city][1]
        def getWindSpeed(self) :
                return self.weather_data [self.city][2]
                




