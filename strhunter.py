# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 01:33:00 2015

@author: matty
"""

import requests

url = "https://zilyo.p.mashape.com/search"

querystring = {"latitude":"38.889931","longitude":"-77.009003","maxdistance":"11.25","provider":"airbnb","sort":"high2low","resultsperpage":"1","page":"1"}

headers = {
    'x-mashape-key': "5BrRximyJgmshtkDZpAPKxGNpoPNp1n4MEHjsnSvvYjOBagtba",
    'accept': "application/json"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#def _get_paginated(self, url, params=None):
#     while True:
#         page = self.get(url, params=querystring).json()
#
#         for item in page["values"]:
#             yield item
#
#        if "next" in page:
#            url = page["next"]
#             params = None
#         else:
#             break

#print(response.text)
json_string=(response.text)
import json
parsed_json = json.loads(json_string)
#parsed_json.keys()
#print parsed_json
print (parsed_json[u'propType'])