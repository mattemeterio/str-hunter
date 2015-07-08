# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 01:33:00 2015

@author: matty
"""

import requests
import json
import csv
import sys
import fileinput


url = "https://zilyo.p.mashape.com/search"

querystring = {"latitude":"38.889931","longitude":"-77.009003","maxdistance":"11.25","provider":"airbnb","sort":"high2low","resultsperpage":"2","page":"1"}

headers = {
    'x-mashape-key': "5BrRximyJgmshtkDZpAPKxGNpoPNp1n4MEHjsnSvvYjOBagtba",
    'accept': "application/json"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# start of pagination shit from kazanir
# def _get_paginated(self, url, params=None):
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
# end of pagination shit from kazanir

# print(response.text)
json_string=(response.text)
parsed_json = json.loads(json_string)

# start of csv export conversion demo
# l = []
# for line in fileinput.input():
#     l.append(line)
# myjson = json.loads(''.join(l))
# keys = {}
# for i in myjson:
#     for k in i.keys():
#         keys[k] = 1
# mycsv = csv.DictWriter(sys.stdout, fieldnames=keys.keys(),
#                        quoting=csv.QUOTE_MINIMAL)
# mycsv.writeheader()
# for row in myjson:
#     mycsv.writerow(row)
# end of csv export conversion demo

# github test line
print parsed_json[u'result'][0][u'priceRange'][0][u'monthly']
print parsed_json [u'result'][1][u'priceRange'][0][u'monthly']