import json
import requests
import http.client
import access_codes

def get_external_ip():
    r = requests.get('https://myexternalip.com/raw')
    return r.content.decode('utf-8')

clientid, oauth_token = access_codes.channel_codes()
auth = {'Client-ID': clientid, 'Authorization' : 'Bearer {}'.format(oauth_token)} 
callback = 'http://'+get_external_ip()+':8000'
url = 'https://api.twitch.tv/helix/webhooks/hub'

def suscribe_to_get_followers():

    mode = 'subscribe'    
    print("callback to: "+callback)
    headers = {'Client-ID': clientid, 'Authorization' : 'Bearer {}'.format(oauth_token),
               'Content-type': 'application/json'}
         
    topic = 'https://api.twitch.tv/helix/users/follows?first=1&to_id=153781693'

    foo = { 'hub.mode':mode,
            'hub.topic':topic,
            'hub.callback':callback,
            'hub.lease_seconds' : 86400
            }

    json_foo = json.dumps(foo)
    
    connection = http.client.HTTPSConnection('api.twitch.tv')
    connection.request('POST', '/helix/webhooks/hub' ,body=json_foo, headers=headers)
    response = connection.getresponse()
    print(response.status, response.reason)
    print(response.read().decode())
    return callback
