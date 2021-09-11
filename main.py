import requests
from googletrans import Translator
translator = Translator()
api_key = "Sua API"
base_url = ("http://api.openweathermap.org/data/2.5/weather?")
city_name = ("Sua Cidade")
complete_url = str(base_url + "q=" + city_name + '&appid=' + api_key)
response = requests.get(complete_url)

x = response.json()

if x['cod'] != '404':
    y = x['main']
    concurrent_temp = y['temp']
    concurrent_pres = y['pressure']
    concurrent_hum = y['humidity']

    z = x['weather']
    #Traduzindo a descricao para portugues
    weather_descr = (z[0]['description'])
    translation = translator.translate(weather_descr, dest='pt')
    
    #Temperatura no site é dada em Kelvins, a formula usada é para transformar em Celsius
    print('Temperatura: ' +str(round(concurrent_temp-273))+'°C',
          '/\nPressao: ' + str(concurrent_pres)+'hPa',
          '\nHumidade: ' + str(concurrent_hum)+'%',
          '\nPrevisao: ' + (translation.text))
else:
    print('Cidade nao encontrada')
