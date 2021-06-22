import os
import requests
from datetime import datetime

def cls():
    os.system("cls")

def clear_latest():
    file = open("Latest_Result.txt", "r+")
    file.truncate(0)


def append(text):
      with open("Latest_Result.txt", "a") as e:
        e.write(text)

def append_to_history():
    with open("History.txt", 'r+') as f:
     with open("Latest_Result.txt", 'r+') as g:
      content_new = g.read()
      content_old = f.read()
      f.seek(0, 0)
      f.write(content_new.rstrip('\r\n') + '\n' + content_old)
      f.close()

def repeat():
    e = input("Do you want to re-try? (type yes/no) ")
    if e.upper() == "YES":
        cls()
        main()
    elif e.upper() == "NO":
        return
    else:
        print("Please enter correct response")
        repeat()

def main():
    location = input("Enter the city name: ")
    clear_latest()
    cls()
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+"31ae3f3267ce2a28b334bd9864986365"
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    cod = api_data['cod']
    if 300<int(cod)<600:
        message = api_data['message']
        print(message)

        error = "-------------------------------------------------------------\n"+ date_time + "\n" + message + "\n-------------------------------------------------------------"
        with open("History.txt", 'r+') as z:
            content_old = z.read()
            z.seek(0, 0)
            z.write(error.rstrip('\r\n') + '\n' + content_old)
            z.close()
        repeat()
    else:
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        preasure = api_data['main']['pressure']


        print ("-------------------------------------------------------------")
        print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
        append ("-------------------------------------------------------------\nWeather Stats for - {}  || {}".format(location.upper(), date_time))
        print ("-------------------------------------------------------------")

        print ("Current temperature is: {:.2f} deg C".format(temp_city))
        append ("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
        print ("Current weather desc  :",weather_desc)
        append ("\nCurrent weather desc  :" + weather_desc)
        print ("Current Humidity      :",hmdt, '%')
        append ("\nCurrent Humidity      :" + str(hmdt) + '%')
        print ("Current wind speed    :",wind_spd ,'kmph')
        append ("\nCurrent wind speed    :" + str(wind_spd) + 'kmph')
        print("Atmospheric pressure  :", preasure, 'hPa')
        append("\nAtmospheric pressure  :" + str(preasure) + 'hPa')
        append("\n-------------------------------------------------------------")

        append_to_history()

        repeat()

main()