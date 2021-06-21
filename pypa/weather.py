import pyowm
from notipy.cli import Notipy
import testInternet

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

if not testInternet.is_connected():
    print(RED + 'Internet is not working well! Check your connection.' + NO)
    exit(0)
        
try:   
    owm = pyowm.OWM('b49a211fcc0d10baf99c9f12321e5025') #API key
    observation = owm.weather_at_place('Pokhara,np')
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')
    status = w.get_status()
    detailStatus = w.get_detailed_status()
    print('Today\'s status: ' + status)
    print('Detail Status: ' + detailStatus)
    Notipy().send('Detail Status: ' + detailStatus)
    Notipy().send('Status: ' + status)
    temperature = temperature.pop('temp')
    print('Today\'s temperature in celsius:')
    print(temperature)
    Notipy().send('Temperature: ' + str(temperature))
except KeyboardInterrupt:
    print(RED + '\nClosing!' + NO)
except:
    print(RED + 'An error occured!' + NO)
