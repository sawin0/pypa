import datetime
from notipy.cli import Notipy

now = datetime.datetime.now()
print('Today is : ' + now.strftime('%A'))
Notipy().send('Today is : ' + now.strftime('%A'))
