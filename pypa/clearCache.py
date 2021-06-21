import os
from notipy.cli import Notipy

os.system('chmod 755 clearcache.sh')
print('RAM cache cleared!')
Notipy().send('Cache cleared!')
