import discord
from discord.ext import commands
from environment import get_env
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)
# client = discord.Client(intents=intents)

from discord_events import *



if __name__ == '__main__':
    client.run(get_env().DISCORD_BOT_TOKEN)
