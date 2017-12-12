import datetime
import datastore
import reddit
import config
import requests
import sys

override = False
if len(sys.argv) > 1 and sys.argv[1] == "override":
    override = True

time = datetime.datetime.now().hour

users = datastore.getUsersByTime(time, override)

#reply construction
def response(senderId, articleUrl):
    articleData = {
        "recipient": {
            "id": senderId
        },
        "message": {
            "text": "Here is your link!: "+ articleUrl
        }

    }
    requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + config.PAGE_ACCESS_TOKEN, json=articleData)

for user in users:
    try:
        url = reddit.pick_sub(user["topics"])
        response(user["id"], url)
    except Exception as e:
        print e.message
#Aishwarya worked on this project to provide code on message response structure
