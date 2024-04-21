import os
import json
import asyncio
import discord

from typing import Final
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

with open("data/bot.json", "r") as f:
    config = json.load(f)

prefix = config.get("prefix")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load_cogs()
    await bot.start(TOKEN)

asyncio.run(main())