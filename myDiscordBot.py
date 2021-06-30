import discord
import random
from discord.ext import commands
TOKEN = open("C:/Users/gavin/OneDrive/Documents/token.txt","r").readline()
client = commands.Bot(command_prefix = '.')
@client.command()
async def greet(ctx):
    await ctx.send("Htllo everyone! This is the python built bot of Gavin Johnson, delivering a greeting!")
client.run(TOKEN)
