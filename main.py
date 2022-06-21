#Importing the modules
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse

app = Flask(__name__)

#Post Request Webhook
@app.route('/sms', methods=['POST'])

#Defining the function
def sms():
  resp = MessagingResponse()
  resp.message('Hello, welcome to Twilio Masterclass, your host Rishab here. I have got a gift for you, Twilio Startup credits --> https://twiliostartups.com/collision')
  return str(resp), 200

# Running the Flask web server
if __name__ == '__main__':
    app.run()