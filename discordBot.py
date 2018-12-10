import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from nacl import *
import youtube_dl


TOKEN = 'NTE5NjI4NzIwODI3MjY5MTgw.DuiIiQ.9mqRo2aU3KZcND9Nr76PCqKH7I8'

client = discord.Client()



@client.event

async def on_message(message): 
    v = ["Hello", "hello", "hej"]

    if message.author == client.user: 
        return
    

    if message.content.startswith("Hello"):
        msg = "Fuck off {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith("hello"):
        msg = "Fuck off {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith("hej"):
        msg = "Fuck off {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("add"): 

        channel = client.get_channel('431519138696003588')
        vsg = await client.join_voice_channel(channel)
        player = await vsg.create_ytdl_player('https://www.youtube.com/watch?v=XCPj4JPbKtA')
        player.start()
    if message.content.startswith("bot"):
        client.close()


@client.event
async def on_ready(): 
    print("logged in as")
    print(client.user.name) 
    print(client.user.id)
    print('------')

client.run(TOKEN)
