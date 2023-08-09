import re
import time
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import Request, urlopen


# VARIABLE CONFIG
urlbase = "https://thepiratebay7.com/search/"
searched_phrase = "warszawianka"

# searched_phrase_html = "s01e06"
#text = 'Warszawianka.s01e06.1080p.SKYSHO.MULTi.WEB-DL.AVC.EAC3-BulITWarszawianka.s01e03.1080p.SKYSHO.MULTi.WEB-DL.AVC.EAC3-BulIT'
patterns = ['s01e10']
success_message = "Czas na oglądanie! Nowy odcinek " + searched_phrase + " jest już dostępna na ThePirateBay." 
failure_message = "Niestety, " + searched_phrase + " nie jest jeszcze dostępna na ThePirateBay."
url = urlbase + searched_phrase
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(request_site).read().decode('utf-8')
soup = BeautifulSoup(webpage, "html.parser")
trimmed_html = soup.get_text()
while(True):
    for pattern in patterns: 
        t = time.time()
        print("Current time", time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(t)))
        # print('Looking for "%s" in "%s" ->' % (pattern, trimmed_html), end=' ')
        if re.search(pattern, trimmed_html):
            print(success_message) 
        else:
            print(failure_message)
    time.sleep(300)