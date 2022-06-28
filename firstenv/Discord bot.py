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


def math(numbers):
    if "+" in numbers:
        num_1 = int(numbers[1])
        num_2 = int(numbers[3])
        return num_1 + num_2

    if "-" in numbers:
        num_1 = int(numbers[1])
        num_2 = int(numbers[3])
        return num_1 - num_2

    if "*" in numbers:
        num_1 = int(numbers[1])
        num_2 = int(numbers[3])
        return num_1 * num_2

    if "/" in numbers:
        num_1 = int(numbers[1])
        num_2 = int(numbers[3])
        return num_1 / num_2


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

    # checks to see if the message starts with the command
    if message.content.startswith("!math"):
        # splits the message content and stores is to the numbers variable.
        numbers = message.content.split()
        # passes the numbers variable into the math function and saves it to the result variable
        result = math(numbers)
        # sends the result to the channel that the command was used in which is message.channel
        await message.channel.send(result)


# pulls token from .env and uses it to log into client
client.run(os.getenv("token"))
