import discord
import os
from discord.ext import commands
import requests
import asyncio
from dotenv import load_dotenv()

load_dotenv()

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None)

GUILD_ID = 755793441287438469
CHANNEL_ID = 1073123321090150410


@client.event
async def on_ready():
    os.system('clear')
    print(f'Logged in as {client.user} ({client.user.id})')
    client.dispatch("call")
    await asyncio.sleep(21500)
    
@client.event
async def on_call():
    if client.get_guild(GUILD_ID).get_member(client.user.id).voice is None:
        check = True
        while check:
            try:
                vc = client.get_guild(GUILD_ID).get_channel(CHANNEL_ID)
                await vc.connect()
                check = False
            except:
                await asyncio.sleep(1)
                
@client.event
async def on_voice_state_update(member, before, after):
    if client.get_guild(GUILD_ID).get_member(client.user.id).voice is None:
        check = True
        while check:
            try:
                vc = client.get_guild(GUILD_ID).get_channel(CHANNEL_ID)
                await vc.connect()
                check = False
            except:
                await asyncio.sleep(1)
            

client.run(os.getenv("TOKEN"))
