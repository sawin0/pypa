import pypapath
import os
import testInternet

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

if not testInternet.is_connected():
    print(RED + 'Internet is not working well! Check your connection.' + NO)
    exit(0)
path = pypapath.MODULE_PATH + '/movies.py'
os.system('python ' + path + ' ')
