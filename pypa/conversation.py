from brain import Brain
from notipy.cli import Notipy

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

def handleForever():
    try:
        brain = Brain()
        while True:
            text = input('\n>>> ')
            brain.query(text)
    except:
        print(RED + '\nAssistant is closed' + NO)
        Notipy().send('Assistant is closed!')
        
