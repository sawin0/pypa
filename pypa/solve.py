import re
import sys

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

query = ''
for arg in sys.argv:
   query = query + arg + ' '  

def handle(query):
    expression = re.findall('\s([0-9\+\-/\*\(\)\.\s]+)', query)
    
    if not expression:
        print(RED + 'Please try looking README.md.' + NO)
        return

    expression = expression[0]

    try:
        print(eval(expression))
    except SyntaxError:
        print(RED + 'Invalid Syntax. Enter the valid syntax.' + NO)
        return
    except ZeroDivisionError:
        print(RED + 'A number cannot be divide by zero.' + NO)
        return
handle(query)
