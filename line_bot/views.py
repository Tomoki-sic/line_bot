from django.shortcuts import render

from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


from line_bot.line_message import LineMessage,create_single_text_message
from line_bot.Hotpepper import Hotpepper
# Create your views here.
@csrf_exempt
def message(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        if len(request['events'])!=0:
            data = request['events'][0]
            reply_token = data['replyToken']
            message = data['message']
            obj = Hotpepper()      
            if message['type']=='text':    
                line_message = LineMessage(obj.serch_keyword(message['text']))
            elif message['type']=='location':
                #経度と緯度を獲得
                #ショップのリストを獲得
                line_message = LineMessage(obj.get_shop_list(message['latitude'], message['longitude']))
            else:
                 line_message = LineMessage(create_single_text_message('error'))
            line_message.reply(reply_token)
        return HttpResponse("ok")


#{'destination': 'U8d7576e87a1a0d3ff0c93aa6a365e5f6', 'events': [{'type': 'message', 'message': {'type': 'text', 'id': '15296029753928', 'text': 'あ'}, 'timestamp': 1640258736169, 'source': {'type': 'user', 'userId': 'Ue0198bbb37121d4b833cce8937e2c941'}, 'replyToken': 'fc0fbe354db04bdd9b6de135a723743f', 'mode': 'active'}]}
#{'destination': 'U8d7576e87a1a0d3ff0c93aa6a365e5f6', 'events': [{'type': 'message', 'message': {'type': 'location', 'id': '15296031158906', 'latitude': 35.643297351198505, 'longitude': 139.74958490422705, 'address': '日本、〒108-0023 東京都港区芝浦３丁目９−１４'}, 'timestamp': 1640258752570, 'source': {'type': 'user', 'userId': 'Ue0198bbb37121d4b833cce8937e2c941'}, 'replyToken': 'dcc2568951bb45339d041f8967f91d89', 'mode': 'active'}]}
