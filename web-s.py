import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(
    "https://www.flipkart.com/search?q=gaming+laptops&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_7_na_na_na&as-pos=0&as-type=RECENT&suggestionId=gaming+laptops%7CLaptops&requestId=9fd9855a-3b6b-4131-bdf2-0cddd74c1f05&as-backfill=on")
# https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
    name = a.find('div', attrs={'class': '_3wU53n'})
    price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    rating = a.find('div', attrs={'class': 'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    # ratings.append(rating.text)

df = pd.DataFrame({'Product Name': products, 'Price': prices})
df.to_csv('products.csv', index=False, encoding='utf-8')
