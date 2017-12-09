from flask import Flask
from flask import request
import config
app = Flask(__name__)

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
        if request_json['entry'][0]['messaging'][0]['message']
            senderId = request_json['entry'][0['messaging'][0]['message']['sender']['id']
            all_messages =request_json['entry'][0]['messaging']
            format_response(senderId)
            return "finished"
    except Exception as e:
        print e.message
        return "finished"

#send a response back
def format_response(senderId):
    try:
        stuffToRespond = # enter reddit stuff here
        if
        response(senderId,"here is your surprise article" , reddit article)
        else
            print("sorry some great tragedy has befallen this bot ")
            response_error(senderId)
        return "finished"
    except:
        response_error(senderId)
        print "Some great tragedy has befallen this bot"
#in case of error
def response_error(senderId):
    reply(senderId, "some unexpceted error has occured please try again")

#reply construction
def response(senderId, message, article_url):
	text_data = {
		"recipient": {
			"id": user_id
		},
		"message": {
			"text": message
		}
        "attachment": {
            "url": article_url
        }
	}
	requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + access_token, json=image_data)
