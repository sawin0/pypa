import os
import testInternet

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

if not testInternet.is_connected():
    print(RED + 'Internet is not working well! Check your connection.' + NO)
    exit(0)

os.system('''sudo apt-get update && sudo apt-get upgrade -y && 
    sudo apt-get dist-upgrade -y''')
