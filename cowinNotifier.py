import requests
import time
import datetime
import json
from discord_webhook import DiscordWebhook
while 1:
    t= datetime.datetime.now()
    date=str(t.strftime("%d")+"-"+t.strftime("%m")+"-"+t.strftime("%Y"))

    apiLink='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=394&date='+date
    x = requests.get(apiLink, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}).text
    y = json.loads(x)

    for center in y["centers"]:
        if(center["sessions"][0]["available_capacity"])!=0 :
            print("kara re register")
            messageString="Center : " + center["name"] + "\ncapacity : " + str(center["sessions"][0]["available_capacity"])
            webhook = DiscordWebhook(url='yourwebhook', content=messageString)
            response = webhook.execute()
            print("Webhook called")

    print("hi")
    time.sleep(10)
