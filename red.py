import praw
import re
from discord_webhook import DiscordWebhook
import datetime

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent=""
)
print("Initialized Reddit API")

postsDiscord = []
for submission in reddit.subreddit("MechanicalKeyboards+mechmarket").top('day'):
    if (re.findall("giveaway", submission.title.lower())):
        postsDiscord.append(str("[" + submission.title + "](<https://www.reddit.com" + submission.permalink + ">)"))
print("List of giveaways created")


todaysDate= str(datetime.date.today())
messageString= '**Giveaways in r/MechanicalKeyboards & r/mechmarket  on ' + todaysDate + '**'
for postDiscord in postsDiscord:
    messageString = messageString + "\n" + postDiscord
print("Created the string which will be sent")

webhook = DiscordWebhook(url='', content=messageString)
response = webhook.execute()
print("Webhook called")
