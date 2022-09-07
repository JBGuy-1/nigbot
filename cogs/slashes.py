import discord
from discord import app_commands
from discord.ext import commands

class Slashes(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print ('slashes ready')
    
    @commands.command()
    async def sync(self, ctx)-> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f"{len(fmt)} commands loaded")
    
    @app_commands.command()
    async def king(self, interaction: discord.Interaction):
        await interaction.response.send_message("kong")
    

async def setup(bot):
    await bot.add_cog(Slashes(bot), guilds=[discord.Object(id=953583957579026442)])

