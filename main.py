import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

achievement = ["Legends", "Epic", "Normal"]


@bot.command(name="start")
async def start(ctx):
    ach = random.choice(achievement)
    await ctx.send(f"Your rank is **{ach}**")

    img_name = random.choice(os.listdir('IMG'))
    with open(f'images/{ach}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    return


bot.run("")
