import re
import requests
import schedule
import smtplib
import time
import configparser
from urllib.parse import quote
from email.message import EmailMessage
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import Request, urlopen
from json import load, dump

config = configparser.ConfigParser()
config.read('config.ini')
sections = config.sections()
print("Credentials in config file:", sections)


def init_variables():
    global tg_api_baseurl
    tg_api_baseurl = 'https://api.telegram.org/bot'
    global hungrytesterobot_token
    hungrytesterobot_token = config['HUNGRYTESTEROBOT_CRED']['bot_token']
    global isAvailable
    isAvailable = False
    global warszawiankobot_token 
    warszawiankobot_token= config['WARSZAWIANKOBOT_CRED']['bot_token']
    global warszawiankobot_chatID
    warszawiankobot_chatID = config['WARSZAWIANKOBOT_CRED']['bot_chatID']

init_variables()

def telegram_bot_sendtext(bot_message, only_to_admin=True):
    config = configparser.ConfigParser()
    config.read('config.ini')
    send_text = f"{tg_api_baseurl}{warszawiankobot_token}/sendMessage?chat_id={warszawiankobot_chatID}&parse_mode=Markdown&text={quote(bot_message)}"
    response = requests.get(send_text)
    return response.json()

def get_torrent_magnet_link():
    global isAvailable
    urlbase = "https://thepiratebay7.com/search/"
    searched_phrase = "warszawianka"
    patterns = {"21-08-2023":"s01e11"}
    url = urlbase + searched_phrase
    request_site = Request(url, headers = {"User-Agent": "Mozilla/5.0"})
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


schedule.every(3).minutes.do(get_torrent_magnet_link)
while True:
    schedule.run_pending()
    time.sleep(1)
