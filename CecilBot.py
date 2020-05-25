from config import *
import CommandHelper
from DataBuilder import Data
from twitchio.ext import commands
"""
To-do:
import data into dict from excel files ... DONE!
analyze command syntax
return and print command responses
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


    ### From here, handle messages that start with '!' ####
    # Check to make sure if message is too long, return a list of messages and send messages in order

    # Make try/catch here
    await bot.handle_commands(ctx) # handle defined decorated bot commands
    print(f'{ctx.channel} - {ctx.author.name}: {ctx.content}')


@bot.command()
async def hello(ctx):
    await ctx.channel.send(f"Hi {ctx.author.name}!")


@bot.command()
async def killbot(ctx):
    await exit()


if __name__ == "__main__":
    bot.run()