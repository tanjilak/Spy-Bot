import discord
import os
import asyncio

client = discord.Client()

@client.event
async def on_ready():
  print("Hey it's me {0.user}".format(client))

@client.event
async def on_message(message):
  #ignore message from bot
  if message.author == client.user:
    return
  if message.content.startswith('!assassin'):
    embedIT = discord.Embed(description="Entering kill mode....", color=0x00ff00)
    await message.channel.send(embed=embedIT)
    #wait 5 seconds for next message
    await asyncio.sleep(5)
    await message.channel.send("""There are assassins running loose! Find them before it's too late""")


#prevent 
try:
  client.run(os.environ['TOKENS'])
except:
    os.system("kill 1")
  
  

