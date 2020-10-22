import base64
import re
import threading
import asyncio
import socket
from sys import exit, argv
from PyQt5 import Qt, QtGui
from PyQt5.QtWidgets import *

from CommandHelper import command_parse
from DataBuilder import Data
from config import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # window geometry data
        self.title = "CecilBot Desktop Application"
        self.left = 200
        self.top = 200
        self.width = 350
        self.height = 450

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # ui elements
        self.channelinput = QLineEdit()
        self.channellistbox = QListWidget()
        self.channellistbox.setFont(Qt.QFont('Arial', 25))
        self.selectedchannel = ""
        self.channellist = []
        self.listcount = 0

        # start new thread and run bot in the background
        thread = threading.Thread(target=startbot, daemon=True)
        thread.start()

        # build the UI
        self.createwindow()
        # show program onscreen
        self.show()

    # layout and design of UI
    def createwindow(self):
        vbox = QVBoxLayout()

        titlelabel = QLabel("CecilBot Desktop \nApplication")
        font = QtGui.QFont("Arial", 24, QtGui.QFont.Black)
        titlelabel.setFont(font)
        titlelabel.setAlignment(Qt.Qt.AlignCenter)
        titlelabel.setMargin(10)
        vbox.addWidget(titlelabel)

        addchannellabel = QLabel("Enter the Twitch channel you wish to connect to:")
        addchannellabel.setAlignment(Qt.Qt.AlignCenter)
        addchannellabel.setMargin(5)
        vbox.addWidget(addchannellabel)

        self.channelinput.setPlaceholderText("Enter channel name here")
        vbox.addWidget(self.channelinput)

        addchannelbutton = QPushButton("Add Channel")
        addchannelbutton.clicked.connect(lambda: self.addchannel())
        vbox.addWidget(addchannelbutton)

        vbox.addStretch(1)

        self.channellistbox.setVerticalScrollMode(True)
        self.channellistbox.clicked.connect((self.listview_clicked))
        vbox.addWidget(self.channellistbox)

        removechannelbutton = QPushButton("Remove Channel")
        removechannelbutton.clicked.connect(lambda: self.removechannel(self.selectedchannel))
        vbox.addWidget(removechannelbutton)

        self.setLayout(vbox)
        # self.show()

    # Event: when a channel name is clicked, the value of that line is stored into variable
    def listview_clicked(self):
        item = self.channellistbox.currentItem().text()
        self.selectedchannel = str(item)

    # Event: when clicking 'add channel' on UI
    def addchannel(self):
        if (self.channelinput.text() is not None):
            joinchannel(self.channelinput.text())
            temp = self.channelinput.text().lower()
            self.channellist.append(temp)
            self.channelinput.clear()
            self.populatelistbox()
        else:
            print("Error from UI adding channel")
            print(traceback.print_exc())

    # Event: when clicking the 'remove' channel button
    def removechannel(self, channelname):
        try:
            if ((self.listcount != 0) and (self.channellistbox.currentItem() is not None)):
                self.channellist.remove(self.selectedchannel)
                partchannel(channelname)
                self.populatelistbox()
        except:
            print("Error from UI removing channel")
            print(traceback.print_exc())

    # Populate or re-populate listbox when channel is added or removed
    def populatelistbox(self):
        self.channellistbox.clear()
        self.listcount = 0
        if len(self.channellist) > 0:
            for item in self.channellist:
                self.channellistbox.insertItem(self.listcount, item)
                self.listcount += 1


# ****************************** Bot functionality *************************

# Connect to twitch server using supplied data, and
#   analyze chat messages for potential bot commands.
# Run as thread until program is closed

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

                temp = command_parse(author, message)
                s = str(temp)
                if isinstance(temp, dict):
                    s = ""
                    count = 0
                    for key, value in temp.items():
                        # Get rid of any trailing decimal values
                        tempvalue = re.sub(r"\.0", "", str(value))
                        if len(temp.items()) == 2:
                            # Only print responses for simple commands
                            if count == 1:
                                s += f"{tempvalue}"
                        else:
                            s += "({0}: {1})".format(key, tempvalue)
                        count += 1
                if s != "Null":
                    for i in split_string(s, 500):
                        sock.send((f"PRIVMSG  #{channel} :{i}\r\n").encode('utf-8'))

            else:
                # Show response in terminal window (if displayed on screen)
                print(resp)
    except Exception:
        print(traceback.print_exc())

# send message to twitch server to JOIN a specified channel
def joinchannel(channelname):
    tempchannelname = channelname.lower()
    sock.send(f"JOIN #{tempchannelname}\n".encode('utf-8'))
    sock.send((f"PRIVMSG  #{tempchannelname} :/me is here\r\n").encode('utf-8'))

# # send message to twitch server to PART (leave/disconnect) a specified channel
def partchannel(channelname):
    tempchannelname = channelname.lower()
    sock.send((f"PRIVMSG  #{tempchannelname} :/me is outta here!\r\n").encode('utf-8'))
    sock.send(f"PART #{tempchannelname}\r\n".encode('utf-8'))

# prepare a string and break it up cleanly if longer than specified number of character
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
    App = QApplication(argv)
    window = Window()
    exit(App.exec())

