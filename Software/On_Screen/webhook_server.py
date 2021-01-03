import json
import webhook_client as client
from flask import Flask, request, Response
import socket
import requests
import time
import access_codes

client_id, oauth_token = access_codes.channel_codes()
#hostName = '192.168.0.6'
hostName = '192.168.1.195'
hostPort = 8000
external_ip = client.suscribe_to_get_followers()
filepath = "C:/Git/Stream/Software/On_Screen/"
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.connect((hostName, 3232))
query_url = 'https://api.twitch.tv/helix/users/follows?to_id=153781693'
headers = {'Client-ID' : client_id, 'Authorization' : 'Bearer {}'.format(oauth_token)}
filepath = "C:/Git/Stream/Software/On_Screen/"

app = Flask(__name__)

def initial_startup():
    time.sleep(5)
    r = requests.get(query_url, headers=headers)
    req = r.json()
    # for user in req['data']:
    #     if (not_listed(user['from_name'], file_array())):
    #         serversocket.send(bytes('WEB_FOLLOW:{}'.format(user['from_name']), 'utf-8'))
    #         write_name(user['from_name'])
    #         time.sleep(5)

@app.route('/', methods=['POST'])
def post_response():
        data = request.json['data']
        name = data[0]['from_name']
        if (not_listed(name, file_array()) or name == 'boteymcbotface'):
                serversocket.send(bytes('WEB_FOLLOW:{}'.format(name), 'utf-8'))
                write_name(name)
        return Response(status=200)

@app.route('/', methods=['GET'])
def get_response():
        return Response(response=request.args.get('hub.challenge'), status=200)

def file_array():
    f = open("{}/blacklist.csv".format(filepath), "r+")
    r = f.read()
    stream = r.split(', ')
    f.close()
    return stream

def not_listed(name, blacklist):
    for check in blacklist:
        if (check == name):
            return False
    return True

def write_name(name):
    f = open("{}/blacklist.csv".format(filepath), "a+")
    try:
        f.write(", {}".format(name))
    except:
        print("Chinese Name Probably")
    f.close()

initial_startup()
app.run(host=hostName, port=hostPort)
