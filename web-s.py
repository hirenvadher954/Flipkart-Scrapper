import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime

today = datetime.date.today()
today = list(str(today))
today = ''.join(today)

products = []
prices = []
date = []

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(
    "https://www.flipkart.com/search?q=gaming+laptops&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_7_na_na_na&as-pos=0&as-type=RECENT&suggestionId=gaming+laptops%7CLaptops&requestId=9fd9855a-3b6b-4131-bdf2-0cddd74c1f05&as-backfill=on")
# https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
    name = a.find('div', attrs={'class': '_3wU53n'})
    price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    products.append(name.text)
    prices.append(price.text)
    date.append(today)
    fileName = name.text[0:20]

    df = pd.DataFrame({'Time': date, 'Price': price.text})
   
    df.to_csv(fileName, index=False, encoding='utf-8')
    df = pd.read_csv(fileName)
    # Again opening it for removing same row
    df.drop_duplicates(subset=None, inplace=True)
    df.to_csv(fileName, index=False, encoding='utf-8')
