import sys
import irc.bot
import requests
import socket
import threading
import datetime
import access_codes

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.connect(('192.168.0.6', 3232))

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = "#" + channel
        self.filepath = "C:/Git/Stream/Software/On_Screen/"
        self.zap_used = []

        # Get the channel id, we will need this for v5 API calls
        url = "https://api.twitch.tv/kraken/users?login=" + channel
        headers = {"Client-ID": client_id, "Accept": "application/vnd.twitchtv.v5+json"}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r["users"][0]["_id"]

        # Create IRC bot connection
        server = "irc.chat.twitch.tv"
        port = 6667
        print("Connecting to " + server + " on port " + str(port) + "...")
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, "oauth:"+token)], username, username)
        

    def on_welcome(self, c, e):
        print("Joining " + self.channel)

        # You must request specific capabilities before you can use them
        c.cap("REQ", ":twitch.tv/membership")
        c.cap("REQ", ":twitch.tv/tags")
        c.cap("REQ", ":twitch.tv/commands")
        c.join(self.channel)

    def on_pubmsg(self, c, e):

        # If a chat message starts with an exclamation point, try to run it as a command
        if e.arguments[0][:1] == "!":
            cmd = e.arguments[0].split(" ")[0][1:]
            print("Received command: " + cmd)
            self.do_command(e, cmd)
        return

    def do_command(self, e, cmd):
        cmd = cmd.lower()
        c = self.connection
        name = e.source.split("!")[0]
        split_message = e.arguments[0].split(" ")[1:]
        message = " ".join(split_message)

        if cmd == "c":
            message = "Voted for Cade!"
            c.privmsg(self.channel, message)
            #clientsocket.send(bytes("c", "utf-8"))

        elif cmd == "b":
            message ="Voted for Brandt!"
            c.privmsg(self.channel, message)
            #clientsocket.send(bytes("b", "utf-8"))
        
        elif cmd == "cookie":
            message = "COOKIE FOR {}".format(name)
            c.privmsg(self.channel, message)
            serversocket.send(b'cookie')
        
        elif cmd == "zap":
            if (self.not_listed(name, self.zap_used) or name == 'boteymcbotface'):
                self.zap_used.append(name)
                message = "zapped the twins"
                c.privmsg(self.channel, message)
                serversocket.send(b'zap')
            else:
                message = "Only ONE ZAP 4 U"
                c.privmsg(self.channel, message)

        elif cmd == "idea":
            try:
                self.write_idea(name, message)
                c.privmsg(self.channel, "Thank you for the idea!")
            except:
                c.privmsg(self.channel, "Invalid Suggestion, No Emojis")

        elif cmd == "help":
            c.privmsg(self.channel, "!zap - zap the twins once per stream!cookie - treat yo-self, bottom left!idea - submit an idea")
        
        # The command was not recognized
        else:
            c.privmsg(self.channel, "Did not understand command: " + cmd)

    def not_listed(self, name, blacklist):
        for check in blacklist:
            if (check == name):
                return False
        return True

    def write_idea(self, name, suggestion):
        f = open("{}/shitty_ideas.txt".format(self.filepath), "a+")
        f.write("{} : {}\n".format(name, suggestion))
        f.close()

def main():
    client_id, token = access_codes.bot_codes()
    username  = "BoteyMcBotFace"
    channel   = "reflectwin"

    bot = TwitchBot(username, client_id, token, channel)
    bot.start()

if __name__ == "__main__":
    main()
