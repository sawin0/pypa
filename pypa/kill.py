import pypapath
import os

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

try: 
	os.system('ps -A')
	print(RED+ 'Killing unknown process may harm your Computer!' + NO)
	process = input('Enter the process name you want to kill: ')
	os.system('pkill -9 ' + process)
except:
	print(RED + '\nClosing!' + NO)
	
