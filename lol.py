import requests
import json
import sys
import os

sys.path.append(os.getcwd()) 

summonerName = "freestylinrough"
requestPrefix="https://na.api.pvp.net"
requestSuffix="?api_key="+ apiKey
requestContent="/observer-mode/rest/featured"

requestURL = requestPrefix+requestContent+requestSuffix

print(requestURL)

r=requests.get(requestURL,auth=('user','pass'))
j=json.loads(r.text)

