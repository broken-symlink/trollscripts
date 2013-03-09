#!/usr/bin/python

from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
import webbrowser

keys = open('keys', 'r')
client_key = keys.readline()
client_key = client_key.split()[2]
client_secret = keys.readline()
client_secret = client_secret.split()[2]
keys.close()

url = "https://boredatbutler.com/api/v1/"
request_token_url = url + "oauth/request_token"

# obtain request token
oauth = OAuth1(client_key, client_secret=client_secret)
r = requests.post(url=request_token_url, auth=oauth, verify=False)
content = r.json()
resource_owner_key = content['oauth_token']
resource_owner_secret = content['oauth_token_secret']

# obtain authorization from user
authorize_url = url + "oauth/authorize?oauth_token="
authorize_url = authorize_url + resource_owner_key
webbrowser.open(authorize_url)
input("Press enter after granting access.")

# obtain access token
oauth = OAuth1(client_key, client_secret=client_secret, resource_owner_key=resource_owner_key, resource_owner_secret=resource_owner_secret)
access_token_url = url + "oauth/access_token"
r = requests.post(url=access_token_url, auth=oauth, verify=False)

content = r.json()
resource_owner_key = content['oauth_token']
resource_owner_secret = content['oauth_token_secret']

oauth = OAuth1(client_key, client_secret=client_secret, resource_owner_key=resource_owner_key, resource_owner_secret=resource_owner_secret)
r = requests.get(url+"posts", auth=oauth, verify=False)
print(r.json())
