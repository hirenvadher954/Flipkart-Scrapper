import requests, time, smtplib
from bs4 import BeautifulSoup
from notify_run import Notify
from datetime import datetime

url = "https://www.amazon.in/Philips-DuraPower-Trimmer-BT3211-15/dp/B07D1HRHLV/ref=sr_1_7?crid=3O48QEAI3UZY0&keywords" \
      "=philips+trimmer+for+mens&qid=1581571268&sprefix=philips+trim%2Caps%2C-1&sr=8-7 "
dp = 2000
URL = url
pnmsg = "Below Rs. " + str(dp) + " you can get your Phillips Trimmer."
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

title1 = ""
def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    main_price = price[2:]

    l = len(main_price)  # Converting into Integer (Rupee no symbol remove)
    if l <= 6:
        main_price = price[2:5]
    else:
        p1 = price[2]
    p2 = price[4:7]
    pf = str(p1) + str(p2)
    main_price = int(pf)

    price_now = int(main_price)
    title1 = str(title.strip())
    main_price1 = main_price
    print("Name : " + title1)
    print("CURRENT PRICE : " + str(main_price1))
    print("DESIRED PRICE : " + str(dp))

    count = 0

    if price_now <= dp:
        send_mail()
        push_notification()
    else:
        count += 1


print("Rechecking.." + str(datetime.now()))


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('170390107045@saffrony.ac.in', 'Ahirjsca2')
    subject = "Price of Phillips Trimmer has fallen down below Rs. " + str(dp)
    body = "Hey ! \n  has fallen down below Rs." + str(
        dp) + ".\n So, hurry up & check the amazon link right now : " + url
    msg = f"Subject: {subject} \n\n {body} "
    server.sendmail(
        '170390107045@saffrony.ac.in',
        'hirenjsca@gmail.com',
        msg
    )
    print("Email Mokli Ditho")

    server.quit()


def push_notification():
    notify = Notify()
    notify.send(pnmsg)
    print("HEY Hiren, NOTIFICATION Mokli")
    print("Minute pachi pachi check karse price")


count = 0
while True:
    count += 1
    print("Count : " + str(count))
    check_price()
    time.sleep(60)
