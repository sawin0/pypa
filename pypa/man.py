import os

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

try:
	app = input('Enter the application\'s name to get help/manual: ')
	os.system('man ' + app)
except:
	print(RED + '\nClosing' + NO)
