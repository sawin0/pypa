import datetime
import pypapath
from notipy.cli import Notipy

now = datetime.datetime.now()
print('Current time : ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)) 
Notipy().send('Current time : ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second))
