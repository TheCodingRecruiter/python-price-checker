import random
import time
import requests
from bs4 import BeautifulSoup as bs
from lxml import html
import re




headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}



def check_price():
    URL = 'https://www.amazon.com/ADVANCED-Dual-Control-Electric-Certified-Radiation/dp/B07WC58PQD/ref=sr_1_4?keywords=heated+blanket+queen&qid=1575126371&sr=8-4'
    page = requests.get(URL, headers=headers)

    soup1 = bs(page.content, 'html.parser')
    soup2 = bs(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()
    title = title.strip()

    price = soup2.find(id='priceblock_ourprice').get_text()
    price = price.strip()
    price_re = re.findall(r'\d+\.?\d*', price)
    price = price_re[0]
    price = float(price)
    return price




def run_price_checker():
    minute_length = 60
    day_length = 24
    price = check_price()
    runcount = 0
    loopover = True
    while loopover:
        runcount = runcount + 1
        print(f'{runcount} number of run throughs')
        price = check_price()
        if price < 85:
            loopover = False
            print(f'Buy it Now. It dropped to ${price}')
            print(URL)
        else:
            print(f"Don't buy it yet.  It still costs ${price}")
            time.sleep(minute_length * 10)

run_price_checker()
