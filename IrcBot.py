from config import *
import re
import socket
import base64
import threading
import queue
import traceback
from CommandHelper import *
from time import sleep

"""
    General bot functionality. Not used for GUI operation
"""



sock = socket.socket()
sock.connect((SERVER, PORT))

def startbot():
    try:
        token = base64.b64decode(TMI_TOKEN)
        token = token.decode('ascii')
        sock.send(f"PASS {token}\n".encode('utf-8'))
        sock.send(f"NICK {BOT_NICK}\n".encode('utf-8'))

        while True:
            resp = sock.recv(2048).decode('utf-8')

            if resp.startswith('PING'):
                sock.send("PONG :tmi.twitch.tv\n".encode('utf-8'))

            messageformat = ":(.*)\!.*@.*\.tmi\.twitch\.tv\sPRIVMSG\s#(.*)\s:(.*)\r"
            m = re.search(messageformat, str(resp))
            if m:
                author, channel, message = m.groups()
                # print(f"{channel}<-{author}: {message}")

                temp = command_parse(author, message)
                s = str(temp)
                if isinstance(temp, dict):
                    s = ""
                    for key, value in temp.items():
                        if len(temp.items()) == 1:
                            s += f"{value}"
                        else:
                            s += f"<{key}: {value}>"
                if s != "Null":
                    for i in split_string(s, 500):
                        sock.send((f"PRIVMSG  #{channel} :{i}\r\n").encode('utf-8'))

            else:
                print(resp)
    except Exception:
        print(traceback.print_exc())

def joinchannel(channelname):
    tempchannelname = channelname.lower()
    sock.send(f"JOIN #{tempchannelname}\n".encode('utf-8'))
    sock.send((f"PRIVMSG  #{tempchannelname} :test from CecilBot\r\n").encode('utf-8'))

def partchannel(channelname):
    tempchannelname = channelname.lower()
    sock.send((f"PRIVMSG  #{tempchannelname} :CecilBot leaving!\r\n").encode('utf-8'))
    sock.send(f"PART #{tempchannelname}\r\n".encode('utf-8'))

def split_string(message, limit, sep=" "):
    words = message.split()
    if max(map(len, words)) > limit:
        raise ValueError("limit is too small")
    res, part, others = [], words[0], words[1:]
    for word in others:
        if len(sep)+len(word) > limit-len(part):
            res.append(part)
            part = word
        else:
            part += sep+word
    if part:
        res.append(part)
    return res


if __name__ == "__main__":

    thread = threading.Thread(target=startbot)
    thread.start()
    sleep(1)
    joinchannel("greenknight5")


