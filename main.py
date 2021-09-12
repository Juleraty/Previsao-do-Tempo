import requests
from googletrans import Translator

translator = Translator()
api_key = "5f250f4b4a9e7da478c8f060bc013a18"
base_url = ("http://api.openweathermap.org/data/2.5/weather?")
city_name = ("Duque de caxias")
complete_url = str(base_url + "q=" + city_name + '&appid=' + api_key)
response = requests.get(complete_url)

x = response.json()


def temperature():
    concurrent_temp = y['temp']
    # Temperatura em Kelvin para Celsius
    temp = round(concurrent_temp - 273)
    return temp


def pressure():
    concurrent_pres = y['pressure']
    pres = concurrent_pres
    return pres


def humidity():
    concurrent_hum = y['humidity']
    hum = concurrent_hum
    return hum


def city():
    city = x['name']
    return city


def country():
    s = x['sys']
    count = s['country']
    return count


def translater():
    z = x['weather']
    # Traduzindo a descricao para portugues
    weather_descr = (z[0]['description'])
    translation = translator.translate(weather_descr, dest='pt')
    return translation.text

if x['cod'] != '404':
    y = x['main']
    print('Cidade:' + city() + ',' + country(),
          '\nTemperatura: ' + str(temperature()) + '°C',
          '\nPressao: ' + str(pressure()) + 'hPa',
          '\nHumidade: ' + str(humidity()) + '%',
          '\nPrevisao: ' + (translater()))


else:
    print('Cidade nao encontrada')
