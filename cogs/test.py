import discord
from discord.ext import commands
from discord import app_commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready():
        print ('Test cog ready')

    @commands.command()
    async def yeet(self, ctx):
        await ctx.send ("yoink")


async def setup(bot):
    await bot.add_cog(Test(bot))