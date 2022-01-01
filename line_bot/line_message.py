from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json, datetime
from django.template.loader import render_to_string, get_template
import requests

REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"
ACCESSTOKEN = 'zgWR+C034WpP0DQi55Yfejf5rn8GR5q7Er8fftyE9otNZz41YRCsxNTozulsTvINzdIsSvUrnT+0eXqPqa0SgW48ztw4Q3b1EtlznZKiCgxn/Dap+qWkZUpyj15kqs5YECC25q/0Gs43YT6DcimPGgdB04t89/1O/w1cDnyilFU='
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ACCESSTOKEN
}

class LineMessage():
    def __init__(self, messages):
        self.messages = messages


    def reply(self, reply_token):
        body = {
            "replyToken": reply_token,
            "messages": self.messages
        }
        print(json.dumps(body).replace("True","true"))
        req = requests.post(REPLY_ENDPOINT_URL, headers=HEADER, data=json.dumps(body).replace("True","true"))

def create_single_text_message(message):
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message


def create_list_text_message(message):
    text = ''
    for mes in message:
        text += (mes+',')
    print(text)
    test_message = [
                {
                    'type': 'text',
                    'text': text
                }
            ]
    return test_message

