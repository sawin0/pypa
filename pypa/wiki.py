from wikipedia import *
import os
import testInternet

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

if not testInternet.is_connected():
    print(RED + 'Internet is not working well! Check your connection.' + NO)
    exit(0)
    
try:
    word = input("\nEnter the word or name you want to search: ")
    print(wikipedia.summary (word, sentences = 20))
except KeyboardInterrupt:
    print(RED + '\nClosing!' + NO)
except PageError:
    print(RED + 'The word you enter isn\'t valid!' + NO)
    print('Related to ' + word)
    print(wikipedia.search (word))
except:
    print(RED + '\nAn Error occured!' + NO)

