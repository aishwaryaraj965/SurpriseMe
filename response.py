import datetime
import datastore
import reddit
import config
import requests

time = datetime.datetime.now().hour

users = datastore.getUsersByTime(time)


for user in users:
    try:
        url = reddit.pick_sub(user["topics"])
        response(user["id"], url)
    except Exception as e:
        print e.message


#in case of error
# def response_error(senderId):
# 	errorData = {
# 		"recipient": {
# 			"id": senderId
# 		},
# 		"message": {
# 			"text": "Here is your surprise article: "+ article_url
# 		}
#
# 	}
# 	requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + config.PAGE_ACCESS_TOKEN, json=articleData)

#reply construction
def response(senderId, article_url):
	articleData = {
		"recipient": {
			"id": senderId
		},
		"message": {
			"text": "Here is your surprise article: "+ article_url
		}

	}
	requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + config.PAGE_ACCESS_TOKEN, json=articleData)
