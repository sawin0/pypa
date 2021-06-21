import facebook
import os
from notipy.cli import Notipy
import pypapath
import testInternet

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red
    
def handle():
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        HOME_DIR = os.environ['HOME']
        os.chdir(HOME_DIR)
        print('''Do you have access token?
    If no, then goto https://developers.facebook.com/tools/explorer 
    and click on 'Get Token' button then click on 'Get User Access Token' 
    and on the User Data Permissions mark on 'pubish_actions'
            ''')
        imageName = input('Enter the image name with extension: ')
        imageLocation = input('Enter the image location: ')
        os.chdir(imageLocation)
        caption = input('Enter the caption to the image: ')
        token = input('Enter Facebook access token: ')
        graph = facebook.GraphAPI(access_token = token)
        graph.put_photo(image=open(imageName, 'rb'), message= caption)
        print('Your photo is uploaded!')
        Notipy().send('Your photo is uploaded!')
    except FileNotFoundError:
        print(RED + 'No such file or directory!' + NO)
    except:
        print(RED + '\nClosing' + NO)
        
if not testInternet.is_connected():
    print(RED + 'Internet is not working well! Check your connection.' + NO)
    exit(0)
handle()
