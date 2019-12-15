import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Apple-MacBook-1-8GHz-dual-core-Intel/dp/B07211W6X2/ref=sxin_0_ac_d_rm?ac_md=0-0-bWFj-ac_d_rm&keywords=mac&pd_rd_i=B07211W6X2&pd_rd_r=1148d494-32e6-45c5-8329-293cad65a21d&pd_rd_w=vyXCu&pd_rd_wg=vczrW&pf_rd_p=6d29ef56-fc35-411a-8a8e-7114f01518f7&pf_rd_r=A00BA435Q117CAM7KXJM&psc=1&qid=1576378749&smid=ATVPDKIKX0DER'


headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36' }

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_dealprice").get_text()
    converted_price = float(price[1:5])

    print(converted_price)
    print(title.strip())

    if(converted_price < 700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('leodini@hotmail.com', '1qaz2wsx3edc')

    subject = 'price fell down!'
    body = 'Ceck the amazon link ' + URL
    msg = 'Subject:' + subject + body
    # msg = f'Subject: {subject}{body}'

    server.sendmail(
        'leodini@hotmail.com',
        'leodini@hotmail.com',
        msg
    )

    print('EMAIL HAS BEEN SENT')

    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60 * 24)