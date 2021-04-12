import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook
import datetime

actualUrl=""

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

    webhook = DiscordWebhook(url='', content=messageString)

    response = webhook.execute()
    print("Webhook called")
else :
    print("Pricce is above Rs. 500")
