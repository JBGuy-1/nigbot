import discord
from discord.ext import commands
import random



class Owner(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print ('owner cog ready')

    ## load
    @commands.command()
    @commands.is_owner()
    async def load(self,ctx, extension):
        try:
            await self.bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send("couldn't load cog")
            return
        await ctx.send("loaded cog")

    ## unload
    @commands.command()
    @commands.is_owner()
    async def unload(self,ctx, extension):
        try:
            await self.bot.unload_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send("couldn't unload cog")
            return
        await ctx.send("unloaded cog")

    ## reload cog
    @commands.command()
    @commands.is_owner()
    async def reload(self,ctx, extension):
        try:
            await self.bot.reload_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send("couldn't reload cog")
            return
        await ctx.send("reloaded cog")

async def setup(bot):
    await bot.add_cog(Owner(bot))