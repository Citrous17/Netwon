# bot.py
import os
import math
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!Newton ')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="add")
async def addition(ctx, num1: float, num2: float):
    response = num1 + num2
    await ctx.send(response)

@bot.command(name="Compute")
async def computation(ctx, problem):
    ans = 0
    if("+" in problem):               
        problemArray = problem.split('+')
        for i, v in enumerate(problemArray):
            problemArray[i] = float(v)
        ans += math.fsum(problemArray)
    response = "```\n" + str(problem) + "\n" + str(ans) + "```"
    await ctx.send(response)

@bot.command(name="info")
async def information(ctx):
    response = "I am a bot that can help you with your math homework!"
    await ctx.send(response)

bot.run(TOKEN)