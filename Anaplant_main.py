import requests
import base64


url = ""
#r = rq.get(url)

def define_user():
    username = input("enter username:")
    return(username)

def define_password():
    password = input("enter password:")
    return(password)

def get_token():
    requests.post("https://auth.anaplan.com/token/authenticate")
    pass




username = "alexander.powers@freseniusmedicalcare.com" #define_user()

# If using cert auth, replace cert.pem with your pem converted certificate
# filename. Otherwise, remove this line.
#cert = open('cert.pem').read()

# If using basic auth, insert your password. Otherwise, remove this line.
password = define_password()

# Uncomment your authentication method (cert or basic). Remove the other.

#user = 'AnaplanCertificate ' + str(base64.b64encode((
#f'{username}:{cert}').encode('utf-8')).decode('utf-8'))

user = 'Basic ' + str(base64.b64encode((f'{username}:{password}').encode('utf-8')).decode('utf-8'))


getHeaders = {
    'Authorization': user
}

getWorkspaces = requests.get('https://api.anaplan.com/1/3/workspaces', headers=getHeaders)

with open('workspaces.json', 'wb') as f:
    f.write(getWorkspaces.text.encode('utf-8'))
