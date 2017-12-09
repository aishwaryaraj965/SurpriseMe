from flask import Flask
from flask import request
import config
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
	app.run()

@app.route("/surpriseme/")
def verify():
    if config.VERIFY_TOKEN == request.args.get('hub.verify_token'):
        return request.args.get('hub.challenge')
    return ''
