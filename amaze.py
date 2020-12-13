import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook
import datetime

actualUrl="https://www.amazon.in/dp/B01J1CFOA8/ref=twister_B07KKWDQFW?_encoding=UTF8&psc=1"

try :
    title = ""
    price = ""
    url = urlopen(actualUrl)
    bs = BeautifulSoup(url,'html.parser')
    title = bs.find('span',{'id' : 'productTitle'}).get_text().strip()
    price = bs.find('span',{'id' : re.compile('priceblock*') }).get_text()
    price = price[2:len(price)]
    currentProduct=title+" : "+price
    print("Product acquired -",currentProduct)
except HTTPError as e :
    print(e)

if (float(price)<500):
    todaysDate= str(datetime.date.today())
    messageString = "[" + str(title) + "](<" + str(actualUrl) + ">) is on sale at **Rs. " + str(price) + "**"
    print("Created the string which will be sent")

    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/776927456271532042/jsMjMOiHu7q2wjwW-rBfSlLpABEQ6U6IqcjjOSdYJYeZiSh6zgfbzrQB53C3v1Qmb0Af', content=messageString)

    response = webhook.execute()
    print("Webhook called")
else :
    print("Pricce is above Rs. 500")
