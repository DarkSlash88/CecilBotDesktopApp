import base64
import re
import threading
import asyncio
from sys import exit, argv
from PyQt5 import Qt, QtGui
from PyQt5.QtWidgets import *

from IrcBot import *
from CommandHelper import command_parse
from DataBuilder import Data
from config import *


"""
To-do:
import data into dict from excel files ... DONE!
analyze command syntax...DONE
return and print command responses - Check message length...Done
encrypt oauth token...Done
build UI...done
pretty print data... in progress

"""

# ******************************** Bot UI **********************************



class Window(QWidget):
    def __init__(self):
        super().__init__()

        # window geometry data
        self.title = "CecilBot Desktop Application"
        self.left = 200
        self.top = 200
        self.width = 350
        self.height = 450

        self.channellist = []
        self.listcount = 0

        # ui elements
        self.channelinput = QLineEdit()
        self.channellistbox = QListWidget()
        self.selectedchannel = ""

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # ***************** Bot data **********************************
        QApplication.processEvents()
        # startbot()
        thread = threading.Thread(target=startbot, daemon=True)
        thread.start()

        # build the UI
        self.createwindow()
        # show program onscreen
        self.show()

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
        self.show()

    def listview_clicked(self):
        item = self.channellistbox.currentItem().text()
        print(item)
        self.selectedchannel = str(item)

    def addchannel(self):
        if (self.channelinput.text() is not None):
            joinchannel(self.channelinput.text())

            self.channellist.append(self.channelinput.text())
            self.channellistbox.insertItem(self.listcount, self.channelinput.text())
            self.listcount += 1
            self.channelinput.clear()
        else:
            print("Error from UI adding channel")

    def removechannel(self, channelname):
        try:
            if ((self.listcount != 0) and (self.channellistbox.currentItem() is not None)):
                self.channellist.remove(self.selectedchannel)
                # print(self.channellist)
                self.listcount = len(self.channellist)
                # print(self.listcount)
                self.channellistbox.clear()
                # print("clear listbox")
                count = 0
                if (len(self.channellist) > 0):
                    for i in self.channellist:
                        if count < self.listcount:
                            self.channellistbox.insertItem(count, str(i))
                            count += count
                else:
                    print("empty")
                partchannel(channelname)
        except:
            print("Error from UI removing channel")


# ****************************** Bot functionality *************************

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
    App = QApplication(argv)
    window = Window()
    exit(App.exec())

