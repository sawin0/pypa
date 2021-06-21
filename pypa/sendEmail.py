import smtplib, getpass
from notipy.cli import Notipy
import testInternet

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

def handle():
    try:
        print("""Please make sure you have Allowed less secure apps: ON
        If you haven't then click on below link and search for 
        "Allow less secure apps: OFF" and trun it on.
        https://myaccount.google.com/security
        """)
        sender = input('Enter your e-mail: ')
        password = getpass.getpass('Enter your password: ')
        receiver = input('Enter receiver\'s e-mail: ')
        content = input('Enter your message: ')
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender, password)
        mail.sendmail(sender, receiver, content)
        mail.close()
        Notipy().send('E-mail is sent!')
        print('E-mail is sent!')
    except KeyboardInterrupt:
        print(RED + '\nClosing!' + NO)    
    except:
        print(RED + '\nAn Error Occured!' + NO)  

if not testInternet.is_connected():
    print(RED + 'Internet is not working well! Check your connection.' + NO)
    exit(0)
handle()
