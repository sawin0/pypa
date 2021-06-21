import facebook
import pypapath
from notipy.cli import Notipy
import testInternet

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

def handle():
    try:
        print('''Do you have access token?
        If no, then goto 
        https://developers.facebook.com/tools/explorer 
        and click on 'Get Token' button then click on 'Get User Access Token' 
        and on the User Data Permissions mark on 'pubish_actions'
        ''')
        status = input('Enter your status: ')  
        token = input('Enter Facebook access token: ')
        graph = facebook.GraphAPI(access_token = token)
        graph.put_object(parent_object='me', connection_name='feed', message=status)
        print('Your status is posted!')
        Notipy().send('Your status is posted!')
    except:
        print(RED + '\nClosing!' + NO)

if not testInternet.is_connected():
    print(RED + 'Internet is not working well! Check your connection.' + NO)
    exit(0)
       
handle()
