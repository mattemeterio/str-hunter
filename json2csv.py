__author__ = 'Matty'
import json
import csv
import requests

url = "https://zilyo.p.mashape.com/search"

querystring = {"latitude":"38.889931","longitude":"-77.009003","maxdistance":"11.25","provider":"airbnb","sort":"high2low","resultsperpage":"2","page":"1"}

headers = {
    'x-mashape-key': "5BrRximyJgmshtkDZpAPKxGNpoPNp1n4MEHjsnSvvYjOBagtba",
    'accept': "application/json"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

parsed_json = json.loads(response.text)
# f = open('test.json')
# data = json.load(f)
# f.close()

# f=csv.writer(open('test.csv','wb+'))
# parsed_json=csv.writer(open('test.csv','wb+'))
# for item in parsed_json:
#     parsed_json.writerow([item['pk'], item['model']] + item['fields'].values())
print parsed_json