import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("Hey it's me {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!start'):
    await message.channel.send('Welcome to SpyBot!')

client.run(os.environ['TOKEN'])
  
  

