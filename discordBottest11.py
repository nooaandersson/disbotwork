import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import discord
from discord import *
import asyncio
from nacl import *
import youtube_dl 


startup_extensions = ["Music"]

TOKEN = 'NTE5NjI4NzIwODI3MjY5MTgw.DuiIiQ.9mqRo2aU3KZcND9Nr76PCqKH7I8'

client = commands.Bot(command_prefix = ".")
app = discord.Client()




@client.event
async def on_ready(): 
    print("bot is ready")

class Main_Commands():
    def __init__(self, client):
        self.client = client

#@client.command(pass_context=True)
#async def on_message(message):

     #if message.content.startswith("https://www.youtube.com"):
        #msg = "Fuck off {0.author.mention}".format(message)
        #await client.send_message(message.channel, msg)
        #global i
        #i = message.content
         

     #await client.process_commands(message)





#@client.command(pass_context=True)
#async def join(ctx):
    
    #channel = ctx.message.author.voice.voice_channel
    #vc = await client.join_voice_channel(channel)
    #player = await vc.create_ytdl_player(i)
    #player.start()
        

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice = client.voice_client_in(server)
    await voice.disconnect()

if __name__ == "__main__": 
    for extension in startup_extensions: 
        try: 
            client.load_extension(extension)
        except Exception as e: 
            exc = '{}: {}'.format(type(e).__name__, e)
            print('failed to load {}\n{}'.format(extension, exc))


client.run(TOKEN)
app.run(TOKEN)
