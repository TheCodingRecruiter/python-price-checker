import random
import time
import requests
from bs4 import BeautifulSoup as bs
from lxml import html
import re


class AmazonProduct:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

    def __init__(self, URL):
        self.URL = URL
        





    def check_price(self):
        URL = self.URL
        page = requests.get(URL, headers=self.headers)

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




    def run_price_checker(self):
        minute_length = 60
        day_length = 24
        price = self.check_price()
        runcount = 0
        loopover = True
        while loopover:
            runcount = runcount + 1
            print(f'{runcount} number of run throughs')
            price = self.check_price()
            if price < 85:
                loopover = False
                print(f'Buy it Now. It dropped to ${price}')
                print(URL)
            else:
                print(f"Don't buy it yet.  It still costs ${price}")
                time.sleep(minute_length * 10)

blanket = AmazonProduct('https://www.amazon.com/ADVANCED-Dual-Control-Electric-Certified-Radiation/dp/B07WC58PQD/ref=sr_1_4?keywords=heated+blanket+queen&qid=1575126371&sr=8-4')

gloves = AmazonProduct('https://www.amazon.com/dp/B01M0SF4ZP/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B01M0SF4ZP&pd_rd_w=EtM44&pf_rd_p=45a72588-80f7-4414-9851-786f6c16d42b&pd_rd_wg=aQCjF&pf_rd_r=YEXGNDMRQS9DT2B9GK58&pd_rd_r=1fe429c7-fe3b-430b-94e5-d9f60377f3d7&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVkIxSjFJMkpER1Y2JmVuY3J5cHRlZElkPUEwMzE0NjEzRDNRMUFUMDFENVpSJmVuY3J5cHRlZEFkSWQ9QTEwMTAxNzAxS05EQVpZUDNPMUdRJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==')

gloves.run_price_checker()

blanket.run_price_checker()
