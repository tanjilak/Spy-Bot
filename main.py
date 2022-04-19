import discord
import os
import asyncio
from discord_components import *


client = discord.Client()
bot = ComponentsBot(command_prefix = "!")

@client.event
async def on_ready():
  print("Hey it's me {0.user}".format(client))
  DiscordComponents(bot)
 

@client.event
async def on_message(message):
  #ignore message from bot
  if message.author == client.user:
    return
  if message.content.startswith('!assassin'):
    embedIT = discord.Embed(title="Starting the Game", description="Entering kill mode....", color=0x900603)
    await message.channel.send(embed=embedIT)
    #wait 5 seconds for next message
    await asyncio.sleep(5)
   
    await message.channel.send("""Please choose what you will like to be assigned as""", 
    components =[ActionRow(
      Button(label="assassin", custom_id="button1", style=ButtonStyle.red),
      Button(label="police", custom_id="button2", style=ButtonStyle.blue),  
      Button(label="regular", custom_id="button3"))],)
    

#prevent rate limit
try:
  client.run(os.environ['TOKENS'])
except:
    os.system("kill 1")
  
  

