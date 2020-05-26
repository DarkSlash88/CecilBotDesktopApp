import twitchio

from config import *
from CommandHelper import command_parse
from DataBuilder import Data
from twitchio.ext import commands
import re

"""
To-do:
import data into dict from excel files ... DONE!
analyze command syntax...DONE
return and print command responses - Check message length
build UI

"""

global data
data = Data()

# ****************************** Bot functionality *************************
#
bot = commands.Bot(
    irc_token=TMI_TOKEN,
    client_id=CLIENT_ID,
    nick=BOT_NICK,
    prefix=BOT_PREFIX,
    initial_channels=CHANNEL
)


@bot.event
async def event_ready():
    print(f"{BOT_NICK} is online!")
    ws = bot.ws
    'Called once when the bot goes online.'
    await ws.send_privmsg("greenknight5", "/me is initialized, awaiting commands.")


@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == BOT_NICK.lower():
        return

    # print(f'{ctx.channel} - {ctx.author.name}: {ctx.content}')
    temp = (re.sub(r"[{|}]", "", str(command_parse(ctx.content))))

    for i in split_string(temp, 400):
        await ctx.channel.send(i)
        print(i)

    # Not needed
    # await bot.handle_commands(ctx) # handle defined decorated bot commands


# @bot.command()
# async def hello(ctx):
#     await ctx.channel.send(f"Hi {ctx.author.name}!")
#
#
# @bot.command()
# async def killbot(ctx):
#     await exit()

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
    bot.run()
