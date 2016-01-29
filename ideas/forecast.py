#!/usr/bin/python
import requests
from requests.auth import AuthBase
import hmac
import hashlib
import time

#class ForecastRESTClient:
#    def __init__(self,key, secret):
#        self.key = key
#        self.secret = secret
#        self.url= "http://magicseaweed.com/developer/forecast-api"
#        self.session = requests.Session()
#    def query(self,method,payload={}):
#        url = self.url
#        payload['method'] = method
#        response = self.session.post(url,data=payload,auth=MyCustomAuth(self.key,self.secret))
#        js = response.json()
#        return js
#
#class MyCustomAuth(AuthBase):
#    def __init__(self,api_key,api_secret):
#        self.key = api_key
#        self.secret = secret
#    
#    def __call__(self,r):
#        r.body += '&nonce=%d' % int(time.time())
#        h = hmac.new(bytes(self.secret,'utf-8'), bytes(r.body,'utf-8'), hashlib.sha512).hexdigest()
#        r.headers['Key'] = self.key
#        r.headers['Sign'] = h
#        return r

def timestamp2String(timestamp):
    import datetime
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

fname = "secret_forecast"
with open(fname) as f:
    content = f.readlines()

key = content[0].split(":")[1].rstrip().lstrip().strip()
secret = content[1].split(":")[1].rstrip().lstrip().strip()

import requests

#Defined spots
idBarceloneta = 3535

r = requests.get("http://magicseaweed.com/api/"+str(key)
        +"/forecast/?spot_id="+str(idBarceloneta)
        +"&units=eu"
        +"&fields=timestamp,localTimestamp,"
        +"fadedRating,solidRating,threeHourTimeText,"
        +"wind.*,condition.temperature,"
        +"charts.*")

json_values = r.json()

print json_values

for value in json_values:
    #Parse times
    local_timestamp = value["localTimestamp"]
    print timestamp2String(local_timestamp)





