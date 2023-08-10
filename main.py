import re
import requests
import schedule
import smtplib
import time
from urllib.parse import quote
from email.message import EmailMessage
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import Request, urlopen
from tgtg import TgtgClient
from json import load, dump


def telegram_bot_sendtext(bot_message, only_to_admin=True):
    bot_token = '5905698711:AAEFghdE5bZu6-c4VlIX3EiBV3ExPEcT1io'
    bot_chatID = '1624988567'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + quote(bot_message)
    response = requests.get(send_text)
    return response.json()

def send_message():
    bot_message = "Hello! This is my first Telegram message."
    telegram_bot_sendtext(bot_message)

def get_torrent_magnet_link():
    urlbase = "https://thepiratebay7.com/search/"
    searched_phrase = "warszawianka"
    patterns = {"14-08-2023":"s01e08","21-08-2023":"s01e11"}
    url = urlbase + searched_phrase
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    webpage = urlopen(request_site).read().decode('utf-8')
    soup = BeautifulSoup(webpage, "html.parser")
    trimmed_html = soup.get_text()
    print(time())
    for key, pattern in patterns.items():
        if re.search(pattern,trimmed_html):
            message = "Czas na oglądanie! Nowy odcinek " + pattern + " jest już dostępny na ThePirateBay."
            telegram_bot_sendtext(message)
        else:
            message = "Niestety, odcinek " + pattern + " nie jest jeszcze dostępny na ThePirateBay."
            telegram_bot_sendtext(message)    
    # in this place I should obtain magnet link from trimmed_html var

get_torrent_magnet_link()

'''
while(True):
    for key, pattern in patterns.items():
        t = time.time()
        print("Current time", time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(t)))
        if re.search(pattern, trimmed_html):
            print("Czas na oglądanie! Nowy odcinek " + pattern + " jest już dostępny na ThePirateBay.")
            send_message()
        else:
            print("Niestety, odcinek " + pattern + " nie jest jeszcze dostępny na ThePirateBay.")
    time.sleep(10)
'''
    
'''
Below I will post lines that I have found on watch_script.py file from "am_bot" repository
Desired Telegram bot message would be a link with magnet: URL to searched torrent.
'''
'''
def telegram_bot_sendtext(bot_message, only_to_admin=True):
    bot_token = '5905698711:AAEFghdE5bZu6-c4VlIX3EiBV3ExPEcT1io'
    bot_chatID = '5905698711'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + quote(bot_message)
    response = requests.get(send_text)
    return response.json()

def send_message():
    my_message = "Hello! This is my first Telegram message."
    telegram_bot_sendtext(my_message)




try:
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    # Load credentials from a file
    f = open(os.path.join(path, 'config.json'), mode='r+')
    config = load(f)
except FileNotFoundError:
    print("No files found for local credentials.")
    exit(1)
except:
    print("Unexpected error")
    print(traceback.format_exc())
    exit(1)

try:
bot_token = config['telegram']["bot_token"]
if bot_token == "BOTTOKEN":
    raise KeyError
except KeyError:
    print(f"Failed to obtain Telegram bot token.\n Put it into config.json.")
    exit(1)
except:
    print(traceback.format_exc())
    exit(1)


'''

'''


'''