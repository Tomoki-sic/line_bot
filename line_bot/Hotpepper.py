from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

import os



class Hotpepper():
    api = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key={key}&lat={lat}&lng={lng}&range=4&order=1&format=json"
    api_keyword = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key={key}&keyword={keyword}&order=1&format=json"
    api_key = 'a95877485866e8c1'
    def __init__(self):
        pass

    def get_shop_list(self, lat, lng):
        url = self.api.format(key=self.api_key, lat=lat, lng=lng)
        response = requests.get(url)
        result_list = json.loads(response.text)["results"]["shop"]
        names = [d.get("name") for d in result_list]
        images = [d.get("logo_image") for d in result_list]
        catches = [d.get("catch") for d in result_list]
        urls = [d.get("urls") for d in result_list]
        genre = [d.get("genre")["name"] for d in result_list]
        print(genre)
        size = len(names)
        if size > 12:
            size = 12
        msg = create_flex_messages(names[:size],images[:size],catches[:size],urls[:size],genre[:size])
        return msg
    
    def serch_keyword(self,keyword):
        keyword = keyword.replace("　", " ")
        url = self.api_keyword.format(key=self.api_key, keyword=keyword)
        response = requests.get(url)
        result_list = json.loads(response.text)["results"]["shop"]
        names = [d.get("name") for d in result_list]
        images = [d.get("logo_image") for d in result_list]
        catches = [d.get("catch") for d in result_list]
        urls = [d.get("urls") for d in result_list]
        genre = [d.get("genre")["name"] for d in result_list]
        size = len(names)
        if size > 12:
            size = 12
        msg = create_flex_messages(names[:size],images[:size],catches[:size],urls[:size],genre[:size])
        return msg


def create_flex_message(names,images):
    msg = [
        {
            "type": "flex",
            "altText": "this is a flex message",
            "contents": {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": images,
                            "size": "full",
                            "aspectRatio": "1.91:1"
                        },
                        {
                            "type": "text",
                            "text": names
                        }
                    ]
                }
            }
        }
    ]
    return msg

def create_flex_messages(names,images,catches,urls,genres):
    columns = []
    for name, image, catch,url, genre in zip(names,images,catches,urls,genres):
        if catch == "":
            catch = "No data"
        columns.append({
            "thumbnailImageUrl": image,
            "title": name+"("+genre+")",
            "text": catch,
            "actions": [
                {
                    "type": "uri",
                    "label": "画像提供：ホットペッパー グルメ",
                    "uri": url["pc"]
                }
            ]
        })
    msg = [
        {
            "type": "template",
            "altText": "おすすめレストラン",
            "template": {
                "type": "carousel",
                "columns": columns
            }
        }
    ]
  
    return msg


