from flask import Flask
from flask import request
import config
import datastore
app = Flask(__name__)

ALL_TOPICS = ("sports", "news", "science", "funfacts", "entertainment", "stories", "lifestyle", "health")

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
	app.run()

@app.route("/surpriseme/", methods=["GET"])
def verify():
    if config.VERIFY_TOKEN == request.args.get('hub.verify_token'):
        return request.args.get('hub.challenge')
    return ''

@app.route("/surpriseme/", methods=["POST"])
#process message
def handle_message():
    request_json = request.get_json()
    print(request_json)
    try:
        senderId = request_json['entry'][0['messaging'][0]['sender']['id']
        if "message" in request_json['entry'][0]['messaging'][0]:

            message = request_json['entry'][0]['messaging'][0]["message"]["text"]
            if message[0:10] == "interests ":
                topics = message[10:].split(", ")
                for topic in topics:
                    if topic not in ALL_TOPICS:
                        reply_text(senderId, "Please set your interests like this:\ninterests sports, news, science\n\nPossible interests are:\nsports, news, science, funfacts, entertainment, stories, lifestyle, health")
                        return ""
                datastore.addUser(senderId,topics)


            else:
                reply_text(senderId, "Please set your interests like this:\ninterests sports, news, science\n\nPossible interests are:\nsports, news, science, funfacts, entertainment, stories, lifestyle, health")
        elif "postback" in request_json['entry'][0]['messaging'][0]:
            time = int(request_json['entry'][0]['messaging'][0]["postback"]["payload"])
            datastore.setTime(senderId,time)
            reply_text(senderId, "Your time preferences have been set.")

    except Exception as e:
        print e.message

    return ""



#send a response back
# def format_response(senderId):
#     try:
#         stuffToRespond = # enter reddit stuff here
#         if
#         response(senderId,"here is your surprise article" , reddit article)
#         else
#             print("sorry some great tragedy has befallen this bot ")
#             response_error(senderId)
#         return "finished"
#     except:
#         response_error(senderId)
#         print "Some great tragedy has befallen this bot"
#in case of error
def reply_error(senderId):
    reply_text(senderId, "some unexpceted error has occured please try again")

#reply construction
def reply_text(senderId, message):
	text_data = {
		"recipient": {
			"id": user_id
		},
		"message": {
			"text": message
		}

	}
	requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + config.PAGE_ACCESS_TOKEN, json=text_data)


def reply_time_choice(senderId, message):
	button_data = {
		"recipient": {
			"id": senderId
		},
		"message": {
			"attachment": {
				"type": "template",
				"payload": {
					"template_type": "button",
					"text": "What time would you like your article sent?",
					"buttons": [
						{
							"type":"postback",
							"title": "8 am CST",
							"payload": "14"
						},
						{
							"type":"postback",
							"title": "12 pm CST",
							"payload": "18"
						},
						{
							"type":"postback",
							"title": "8 pm CST",
							"payload": "2"
						}
					]
				}
			}
		}
	}
    requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + config.PAGE_ACCESS_TOKEN, json = button_data)
