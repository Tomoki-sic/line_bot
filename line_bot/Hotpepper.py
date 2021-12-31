from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

import os



class Hotpepper():
    api = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key={key}&lat={lat}&lng={lng}&range=4&order=1&format=json"
    api_key = 'a95877485866e8c1'
    def __init__(self):
        pass

    def get_shop_name_list(self, lat, lng):
        url = self.api.format(key=self.api_key, lat=lat, lng=lng)
        response = requests.get(url)
        result_list = json.loads(response.text)["results"]["shop"]
        return [d.get("name") for d in result_list]
