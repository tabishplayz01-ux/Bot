import discord
from discord.ext import commands
import json
import os

# Config load karein
with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config['TOKEN']
PREFIX = config['PREFIX']
OWNER_ID = config['OWNER_ID']

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'-----------------------------------------')
    print(f'Elysium is online as {bot.user}')
    print(f'Master Owner ID: {OWNER_ID}')
    print(f'-----------------------------------------')
    
    # Slash commands sync karna zaroori hai
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} slash commands.')
    except Exception as e:
        print(e)
        
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over Elysium Universe >help"))

# Global Owner Check Helper
def is_bot_owner(user_id: int):
    return user_id == OWNER_ID

# Cogs automatic load karne ke liye
async def load_extensions():
    if not os.path.exists('./cogs'):
        os.makedirs('./cogs')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded Cog -> {filename[:-3]}')

@bot.event
async def setup_hook():
    await load_extensions()

bot.run(TOKEN)
