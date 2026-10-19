import discord
from discord.ext import commands
import json

with open('config.json', 'r') as f:
    config = json.load(f)

EMOJIS = config['EMOJIS']

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="help", description="Shows the interactive help menu of Elysium.")
    async def help(self, ctx):
        sparkle = EMOJIS.get("sparkle", "✨")
        music_emoji = EMOJIS.get("music", "🎵")
        
        embed = discord.Embed(
            title=f"{sparkle} Elysium Multipurpose Bot - Help Menu {sparkle}",
            description="Welcome to **Elysium**! You can use both traditional prefix (`>`) and modern Slash commands (`/`).",
            color=discord.Color.from_rgb(88, 101, 242)
        )
        
        embed.add_field(
            name="🛡️ Moderation & Security",
            value="`>ban`, `>kick`, `>timeout`, `>purge`\n*Server protection and anti-nuke tools.*",
            inline=False
        )
        
        embed.add_field(
            name="🎟️ Tickets & Setup",
            value="`>ticket`, `>embed`\n*Dropdown/Button tickets & live chat embed builder.*",
            inline=False
        )
        
        embed.add_field(
            name="👥 Welcome & Auto-Roles",
            value="Welcome cards with automated **Human vs Bot** role assignment.",
            inline=False
        )
        
        embed.add_field(
            name=f"{music_emoji} Music & Voice System",
            value="`>play`, `>skip`, `>queue`, `>pause`, `>stop`\n*High quality YouTube & Spotify music player.*",
            inline=False
        )
        
        embed.add_field(
            name="⚙️ Utility & Info",
            value="`>ping`, `>serverinfo`, `>userinfo`\n*General utility commands.*",
            inline=False
        )

        embed.set_footer(
            text=f"Requested by {ctx.author.name} • Elysium Core", 
            icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url
        )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))
