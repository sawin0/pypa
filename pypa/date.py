import time
from notipy.cli import Notipy

localtime = time.asctime( time.localtime(time.time()) )
date = localtime.split()
print('Current date is : ' + date[1] + ' ' + date[2] + ' ' + date[4])
Notipy().send('Current date: ' + date[1] + ' ' + date[2] + ' ' + date[4])
