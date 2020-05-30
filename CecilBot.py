import base64
import re
import threading
import asyncio
from sys import exit, argv

from twitchio.ext import commands

from CommandHelper import command_parse
from DataBuilder import Data
from config import *
from PyQt5 import Qt, QtGui
from PyQt5.QtWidgets import *

"""
To-do:
import data into dict from excel files ... DONE!
analyze command syntax...DONE
return and print command responses - Check message length...Done
encrypt oauth token...Done
build UI
pretty print data

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
        # self.channelinput = QLineEdit()
        self.channelinput = QLineEdit()
        self.channellistbox = QListWidget()
        self.selectedchannel = ""

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # ***************** Bot data **********************************






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
        addchannelbutton.clicked.connect(lambda: self.joinchannel())
        vbox.addWidget(addchannelbutton)

        vbox.addStretch(1)

        self.channellistbox.setVerticalScrollMode(True)
        self.channellistbox.clicked.connect((self.listview_clicked))
        vbox.addWidget(self.channellistbox)

        removechannelbutton = QPushButton("Remove Channel")
        removechannelbutton.clicked.connect(lambda: self.partchannel())
        vbox.addWidget(removechannelbutton)

        self.setLayout(vbox)
        self.show()

    def listview_clicked(self):
        item = self.channellistbox.currentItem().text()
        print(item)
        self.selectedchannel = str(item)

    def joinchannel(self):
        if (self.channelinput.text() is not None):
            addchannel("greenknight5")
            print(result)



            self.channellist.append(self.channelinput.text())
            self.channellistbox.insertItem(self.listcount, self.channelinput.text())
            self.listcount += 1
            self.channelinput.clear()
        else:
            print("Error from UI adding channel")

    def partchannel(self):
        try:
            if ((self.listcount != 0) and (self.channellistbox.currentItem() is not None)):
                self.channellist.remove(self.selectedchannel)
                print(self.channellist)
                self.listcount = len(self.channellist)
                print(self.listcount)
                self.channellistbox.clear()
                print("clear listbox")
                count = 0
                if (len(self.channellist) > 0):
                    for i in self.channellist:
                        if count < self.listcount:
                            self.channellistbox.insertItem(count, str(i))
                            count += count
                else:
                    print("empty")
        # leavechannel(channelname)
        except:
            print("Error from UI removing channel")


# ****************************** Bot functionality *************************

# global data
data = Data()

token = base64.b64decode(TMI_TOKEN)
token = token.decode('ascii')

bot = commands.Bot(
    irc_token=token,
    client_id=CLIENT_ID,
    nick=BOT_NICK,
    prefix=BOT_PREFIX,
    initial_channels=CHANNEL
)

# commands.Bot.event_join()

def startbot():
    bot.run()

@bot.event
async def addchannel(channel):
    try:
        templist = list()
        print(f"test {channel}")
        templist.append(str(channel).lower())
        print(templist)
        temp2 = ["cecil188"]
        await bot.join_channels(temp2)
        print("passed")
        await bot.ws.send_privmsg(str(channel), "/me is initialized, awaiting commands.")
        return True
    except:
        print("error")
        return False

@bot.event
async def leavechannel(channel):
    try:
        templist = list()
        templist.append(channel)
        await bot.ws.send_privmsg(str(channel).lower(), "/me is outta here!.")
        await bot.part_channels(templist)
        return True
    except:
        print("error")
        return False


@bot.event
async def event_ready():
    print(f"{BOT_NICK} is online!")
    ws = bot.ws
    # Called once when the bot goes online.
    await ws.send_privmsg("greenknight5", "/me is initialized, awaiting commands.")

@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == BOT_NICK.lower():
        return
    # print(f'{ctx.channel} - {ctx.author.name}: {ctx.content}')

    #testing
    # if (ctx.content == "join channel"):
    #     await addchannel("cecil188")
    # if (ctx.content == "leave channel"):
    #     await leavechannel("cecil188")

    # parse output to put in () in proper places
    temp = (re.sub(r"['|{|}]", "", str(command_parse(ctx.author.name, ctx.content))))

    # split message if longer than 500 characters
    if (temp != "None"):
        for i in split_string(temp, 500):
            await ctx.channel.send(i)
            print(i)


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
    # thread = threading.Thread(target=startbot, daemon=True)
    # thread.start()
    window = Window()
    exit(App.exec())

