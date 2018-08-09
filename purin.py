#purin bot by mui

import discord
from discord.ext import commands
import asyncio
import time
import os 

Client = discord.Client ()
client = commands.Bot(command_prefix = "#")

@client.event
async def on_ready():
    print ("woof woof!")

#welcome message
@client.event
async def on_member_join(member):
     embed = discord.Embed(title="welcome 🤝", description="**{0.name}** has joined the server.".format(member), color=0X836953)
     await client.send_message(member.server.get_channel("476173627822440450"), embed=embed)

#goodbye message
@client.event
async def on_member_remove(member):
     embed = discord.Embed(title="goodbye 👋", description="**{0.name}** has left the server.".format(member), color=0X836953)
     await client.send_message(member.server.get_channel("476173627822440450"), embed=embed)

client.run(os.getenv('TOKEN'))
