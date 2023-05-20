import discord
from logic import idk
from idk2 import getUserFromMention
import json


client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send(message.author)

    if message.content.startswith("$based"):
        text = idk(str(message.author))
        await message.channel.send(text)
    

    if message.content.endswith("$based"):
        dirt_text = str(message.mentions)
        print(dirt_text)
        name = dirt_text.split()[2].replace("name=","")
        text = idk(name)
        await message.channel.send(text)

    if message.content.endswith("$based leaderboard"):
        with open("users.json","r") as file:
            data = json.load(file)
        await message.channel.send(data)
    

    if message.content == "!stop":
        await client.logout()


client.run("BOT KEY GOES IN HERE")
