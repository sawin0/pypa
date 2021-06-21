import re
import os 
import pypapath

WORDS = {1:'INTRODUCE', 2:'TIME', 3:'WEATHER', 4:'KILL', 5:'MANUAL', 
    6:'SEND EMAIL', 7:'SOLVE', 8:'PC INFO', 9:'DICT', 10:'DAY', 11:'DATE', 
    12:'WIKI', 13:'STATUS', 14:'PICT', 15:'MOVIE', 16:'UPGRADE', 17:'HELP', 
    18:'NEW EMAIL', 19:'CACHE'}
MODULES = {1:'/intro.py', 2:'/time.py', 3:'/weather.py', 4:'/kill.py', 
    5:'/man.py', 6:'/sendEmail.py', 7:'/solve.py', 8:'/pcInfo.py', 9:'/dic.py',
    10:'/day.py', 11:'/date.py', 12:'/wiki.py', 13:'/status.py', 14:'/pict.py', 
    15:'/movie.py', 16:'/upgrade.py', 17:'/help.py', 18:'/receiveEmail.py', 
    19:'/clearCache.py'}

class Brain(object):
   def isValid(self, text, word):
      return bool(re.search(word, text, re.IGNORECASE))   

   def query(self,text):
      for i in WORDS.keys():
         if self.isValid(text, WORDS[i]):
            path = pypapath.MODULE_PATH + MODULES[i]
            try:
               os.system('python3 ' + path + ' ' + text)
            except:
               print('Something went wrong.')
            return      
      print('Please enter "Help" and try again.')
