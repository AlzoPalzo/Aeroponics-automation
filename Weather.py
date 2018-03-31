import requests

apiAddress = 'http://api.openweathermap.org/data/2.5/weather?lat=0.00&lon=0.00&APPID=' #this variable contains the web address of the api from which current weather is obtained(you will need to get your own free api key and set your longtidude and latitude)

def currentConditions():#This is the function which obtains the current weather condition based on your apo address
    global json_data
    global mainWeather
    global temperature
    global humidity
    global tempC
    json_data = requests.get(apiAddress).json()# This line takes the data and puts it into a variable named json_data
    mainWeather = json_data['weather'][0]['main']
    temperature = json_data['main']['temp']
    humidity = json_data['main']['humidity'] #In these lines the data is being parsed to find the relevant information
    tempC = temperature - 273.15 # Converting the temperature from Kelvin to Centigrade


json_data = 'a'
mainWeather = 'a'
temperature = 0.0
humidity = 1
tempC = 0.0#These are the variables to which the current coditions are saved


def connection_check():#This function attempts to connect to the google website to check wether an internet connection is present
    try:
        requests.get("http://google.com", timeout=3)
        return True
    except requests.ConnectionError:
        pass

    return False


def settingValue():#This is the function that checks what the current weather conditions are and returns what a value for which setting should be used
    connected = connection_check()#first the internet connection is checked
    if (connected == True):
        currentConditions()
        if (humidity > 65) and (tempC <= 14):#The setting returned is based on a combination of the current humidity and temperature
            a = 1
        elif (humidity > 65) and (tempC <= 14):
            a = 2
        elif (humidity > 65) and (23 >= tempC > 14):
            a = 3
        elif (humidity <= 65) and (23 >= tempC > 14):
            a = 4
        elif (humidity  <= 65) and (tempC > 23):
            a = 5
        else:
            a = 6
        return a
    else:
        print('There is no connection, using default setting')
        return 7

def printCurrentConditions():#This function simply prints out the current weather conditions
    print('Current weather conditions are: \n', mainWeather, '\n', '{}C'.format(tempC), '\n', '{}%'.format(humidity))


