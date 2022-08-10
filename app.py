from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from testBot import ask, append_interaction_to_chat_log
import os
import openai

app = Flask(__name__)
#web hook
#if bots being dumb change the key
openai.api_key = "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"
@app.route('/testBot', methods = ['POST'])

#including information
def test():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    #append and update the chat log
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer, chat_log)

    msg = MessagingResponse()
    msg.message(answer)
    #routing back to api
    return str(msg)

if __name__ == '__main__':
    app.run(debug=True)
