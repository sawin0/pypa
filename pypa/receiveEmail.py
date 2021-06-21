# -*- coding: utf-8-*-
import imaplib
import email
import getpass
import pypapath
from notipy.cli import Notipy
import testInternet

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

def handle():
    try:
        username = input('Enter e-mail id: ')
        password = getpass.getpass('Enter password: ')
        m = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        m.login(username,password)
        m.select('"[Gmail]/All Mail"')

        result, data = m.uid('search', None, "UNSEEN") # search all email and return uids
        if result == 'OK':
            for num in data[0].split():
                result, data = m.uid('fetch', num, '(RFC822)')
            if result == 'OK':
                email_message = email.message_from_bytes(data[0][1])    # raw email text including headers
                print('From:' + email_message['From'])
        m.close()
        m.logout()
        
    except IndexError:
        Notipy().send('No new emails!')
        print(RED + '\nNo new emails!' + NO) 
    except KeyboardInterrupt:
        print(RED + '\nClosing!' + NO) 
    except:
        Notipy().send('Invalid username or password!')
        print(RED + 'Invalid username or password!' + NO)       

if not testInternet.is_connected():
    print(RED + 'Internet is not working well! Check your connection.' + NO)
    exit(0)
handle()
