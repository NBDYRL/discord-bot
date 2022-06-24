import discord
from dotenv import load_dotenv
import os

load_dotenv()

# this creates the discord client
client = discord.Client()


@client.event
async def on_ready():
    """
    checks if the bot has conected to discord, once it does, print to terminal
    """
    print("We have logged in to Discord")


@client.event
async def on_message(message):
    """
    checks every message sent on the discord server.
    """
    # if the account that sends the message being checked is the bot, ignore it.
    if message.author == client.user:
        return

    if message.content.startswith("!ping"):
        await message.channel.send("pong!")


# pulls token from .env and uses it to log into client
client.run(os.getenv("token"))
