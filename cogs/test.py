import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def yeet(self, ctx):
        await ctx.send ("yoink")


async def setup(bot):
    await bot.add_cog(Test(bot))