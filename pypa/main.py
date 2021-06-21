import os
import pypapath, conversation, brain, testInternet

os.system('clear')

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

 
class PyA(object):
    def run(self):
        if not testInternet.is_connected():
            print(RED + 'Internet is not working well! Check your connection.' + NO)
        print('What can I do for you?')
        conversation.handleForever()

print('''
        ooooooooo.               ooooooooo.        .o.       
       `888   `Y88.             `888   `Y88.      .888.      
        888   .d88' oooo    ooo  888   .d88'     .8"888.     
        888ooo88P'   `88.  .8'   888ooo88P'     .8' `888.    
        888           `88..8'    888           .88ooo8888.   
        888            `888'     888          .8'     `888.  
        o888o           .8'     o888o        o88o     o8888o 
                    .o..P'                                   
                    `Y8P'                                    
                                                                      
        ******************************************************
        *             PYTHON - PERSONAL ASSISTANT            *
        ******************************************************''')

app = PyA()
app.run()
