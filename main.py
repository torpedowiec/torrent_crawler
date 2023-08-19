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
from json import load, dump

isAvailable = False

def telegram_bot_sendtext(bot_message, only_to_admin=True):
    bot_token = '5905698711:AAEFghdE5bZu6-c4VlIX3EiBV3ExPEcT1io'
    bot_chatID = '1624988567'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + quote(bot_message)
    response = requests.get(send_text)
    return response.json()

def get_torrent_magnet_link():
    global isAvailable
    urlbase = "https://thepiratebay7.com/search/"
    searched_phrase = "warszawianka"
    patterns = {"21-08-2023":"s01e11"}
    url = urlbase + searched_phrase
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    webpage = urlopen(request_site).read().decode('utf-8')
    soup = BeautifulSoup(webpage, "html.parser")
    trimmed_html = soup.get_text()
    for key, pattern in patterns.items():
        if re.search(pattern,trimmed_html):
            if not isAvailable:
                message = "Czas na oglądanie! Nowy odcinek " + pattern + " jest już dostępny na ThePirateBay."
                telegram_bot_sendtext(message)
                print("Message sent successfully.")
                isAvailable = True
            else:
                print("Notification has been already sent.")
        else:
            print("Niestety, odcinek " + pattern + " nie jest jeszcze dostępny na ThePirateBay.")
    
schedule.every(10).seconds.do(get_torrent_magnet_link)
while True:
    schedule.run_pending()
    time.sleep(1)