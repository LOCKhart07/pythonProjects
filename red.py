import praw
import re
from discord_webhook import DiscordWebhook
import datetime

reddit = praw.Reddit(
    client_id="MmLnTIBqWkovcA",
    client_secret="HND4mVoNN8FPcUz2J2V7lgzPlF89zg",
    user_agent="android:com.gaw.myredditapp:v0.0.1 (by u/johnylennon)"
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

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/776927456271532042/jsMjMOiHu7q2wjwW-rBfSlLpABEQ6U6IqcjjOSdYJYeZiSh6zgfbzrQB53C3v1Qmb0Af', content=messageString)
response = webhook.execute()
print("Webhook called")