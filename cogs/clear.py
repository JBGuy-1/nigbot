import discord
from discord.ext import commands


class Clear(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['erase', 'format', 'clear'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self,ctx, amount=1):
        self.amount = amount+1
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'cleared {amount} messages ')

async def setup(bot):
    await bot.add_cog(Clear(bot))