import discord
from discord.ext import commands
import random



class Owner(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    ## load cog
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        try:
            self.cog_load(f"cogs.{extension}")
        except Exception as e:
            await ctx.send("couldn't load cog")
            return
        await ctx.send("cog loaded sucessfully")

    # unload cog
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        try:
            self.cog_unload (f"cogs.{extension}")
        except Exception as e:
            await ctx.send("couldn't unload cog")
            return
        await ctx.send("cog unloaded sucessfully")

    ## reload cog
    @commands.command()
    @commands.is_owner()
    async def reload(self,ctx, extension):
        try:
            self.bot.reload_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send("couldn't reload cog")
            return
        await ctx.send("reloaded cog")

async def setup(bot):
    await bot.add_cog(Owner(bot))