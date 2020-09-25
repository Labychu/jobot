import os
import random
# import discord
from discord.ext import commands
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

default_prefix = '!'

bot = commands.Bot(command_prefix=default_prefix)
client = MongoClient("mongodb+srv://mckenzie:29112001@jojo-quotes.n5rr3.mongodb.net/jojo-quotes?\
retryWrites=true&w=majority")
db = client['jojo-quotes']['quotes']


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='q')
async def quote(ctx, *args):
    try:
        chosen_quote = random.choice(list(db.find()))
        content = chosen_quote['content']
        user = chosen_quote['user']
        chapter = chosen_quote['chapter']
        part = chosen_quote['part']
        await ctx.send(f'> {content}\n\n*{user} - chapter {chapter}, part {part}*')
    finally:
        print(args[0])


bot.run(TOKEN)
