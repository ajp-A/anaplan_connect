import requests
from base64 import b64encode
import json
import pandas as pd


token_url = "https://auth.anaplan.com/token/authenticate"
#r = rq.get(url)


def define_user():
    username = input("enter username:")
    return(username)

def define_password():
    password = input("enter password:")
    return(password)

def get_token():
    r = requests.post(token_url, 
    auth=(username , password))
    return r.status_code

def auth_token_basic(username, password):
    user_credentials= b64encode(b'email:password').decode() 
    auth_headers = {} 
    auth_headers['Authorization'] = 'Basic ' + user_credentials
    auth_url = 'https://auth.anaplan.com/token/authenticate'
    auth_json = requests.post(auth_url, headers=auth_headers).json()
    try:
        auth_token = auth_json['tokenInfo']['tokenValue']
        return auth_token
    except KeyError:
        print('No Token Info found - check your credentials?')


username = define_user()
password = define_password()
token = auth_token_basic(username, password)
print(token)

mdl_id = ""
lineitem_url = 'https://api.anaplan.com/2/0/models/{}/lineItems/'.format(mdl_id) 




#user = 'Basic ' + str(base64.b64encode((f'{username}:{password}').encode('utf-8')).decode('utf-8'))


getHeaders = {
    'Authorization': token
}

getWorkspaces = requests.get('https://api.anaplan.com/1/3/workspaces', headers=token)

with open('workspaces.json', 'wb') as f:
    f.write(getWorkspaces.text.encode('utf-8'))
