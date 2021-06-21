import requests, simplejson, psutil
import platform, datetime
from urllib.request import urlopen
import testInternet

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

try:
    print('\nThis module will print your information!')
    print('Platform: ' + platform.system())
    print('Computer\'s name: ' + platform.node())
    print('System\'s release: ' + platform.release())
    print('System\'s version: ' + platform.version())
    print('Machine type i.e bit: ' + platform.machine())
    print('You are running your PC since ' + str(datetime.datetime.fromtimestamp(psutil.boot_time())))
    print('Current CPU utilization is ' + str(psutil.cpu_percent()) + ' percent')
    print('Current memory utilization is ' + str(psutil.virtual_memory()[2]) + ' percent')
    if not testInternet.is_connected():
        print(RED + 'Internet is not working well! Check your connection.' + NO)
        exit(0)
    
    response = urlopen('http://ip-api.com/json/')
    data = simplejson.load(response)
        
    isp = data['isp']
    timezone = data['timezone']
    lon = data['lon']
    lat = data['lat']
    country = data['country']
    city = data['city']
    countrycode = data['countryCode']
    regionName = data['regionName']
    ip = data['query']
        
    print('Your country: ' + country + ' And Country code: ' + countrycode)
    print('Your curent city: ' + city)
    print('Your curent region name: ' + regionName)
    print('Your curent timezone: ' + timezone)
    print('Longitude: ' + str(lon))
    print('Latitude: ' + str(lat))
    print('Your current ISP: ' + isp)
    print('Your IP address: ' + str(ip))
except:
    print(RED + '\nClosing!' + NO)
