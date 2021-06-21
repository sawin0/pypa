from PyDictionary import PyDictionary
import testInternet

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red
if not testInternet.is_connected():
    print(RED + 'Internet is not working well! Check your connection.' + NO)
    exit(0)
    
try:
    dictionary = PyDictionary()
    word = input('Enter the word you want to search: ')
    meaning = dictionary.meaning(word)
    print(meaning)
except KeyboardInterrupt:
    print(RED + '\nClosing!' + NO)  
except:
    print(RED + '\nAn Error Occured!' + NO)
    
