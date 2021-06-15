from flask import *

import requests
with open('config.json','r') as fp:
    creds=json.load(fp)
#print(creds['key'])
search="google.com"
header={'x-apikey':creds['key']}
def getData(search):
    data=requests.request("GET",creds['url']+"search?query="+search,headers=header)
    return data.json()