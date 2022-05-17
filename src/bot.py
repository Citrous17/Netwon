# bot.py
import os
import math
import urllib.parse
import xml.etree.ElementTree as ET
import requests
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
WOLFRAM_TOKEN = os.getenv('WOLFRAM_TOKEN')

bot = commands.Bot(command_prefix='!Newton ')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="Compute")
async def computation(ctx, problem):
    query = problem[problem.find('(')+1:problem.find(')')]
    await ctx.send(query)
    query = urllib.parse.quote(query)
    wolframResponse = processCommand(query, problem)
    await ctx.send(problem)
    response = str(wolframResponse)
    await ctx.send(response)
    
def processCommand(query, command):
    if "ask Wolfram" in command:
        request = "http://api.wolframalpha.com/v2/query?input=" + str(query) + "&appid=" + str(WOLFRAM_TOKEN) + "&format=image"
        return request
        tree = ET.parse(requests.get(request))
        root = tree.getroot()
          
    return "error"
    
@bot.command(name="info")
async def information(ctx):
    response = "I am a bot that specializes in all problems for Calculus 1 and Calculus 2!"
    await ctx.send(response)

bot.run(DISCORD_TOKEN)