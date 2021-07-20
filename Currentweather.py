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
        def defineWeatherData(self, temperature, conditions, windSpeed):
                self.weather_data [self.city] = [temperature, conditions, windSpeed]
                return

def printWeather(weatherData):
        try:
                print('City: ' + weatherData.city)
                print('  Temperature: ' + weatherData.getTemperature())
                print('  Conditions: ' + weatherData.getWeatherConditions())
                print('  Wind: ' + weatherData.getWindSpeed())
        except KeyError as err:
                print('Error: No weather data exists for city')
                
        print()
        return


# Create class instances for 3 cities
# Toronto and Montreal weather data are already defined in the CurrentWeather class
# Ontario weather does not exist (yet)
TorontoWeather = CurrentWeather('Toronto')
MontrealWeather = CurrentWeather('Montreal')
OntarioWeather = CurrentWeather('Ontario')

# Printing data for Toronto and Montreal should work
# Trying to print the non-existent data for Ontario should cause and exception
printWeather(TorontoWeather)
printWeather(MontrealWeather)
printWeather(OntarioWeather)

# Add data for Ontario and try to print again
OntarioWeather.defineWeatherData('14', 'partly cloudy', '6 km/h W')
printWeather(OntarioWeather)
