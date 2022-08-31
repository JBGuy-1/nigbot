import discord
from discord.ext import commands
import random

class Admin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    ## load cog
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        try:
            self.bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send("couldn't load cog")
            return
        await ctx.send("cog loaded sucessfully")

    ## unload cog
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        try:
            self.bot.unload_extension(f"cogs.{extension}")
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

    @commands.command(aliases=['forgive', 'vindicate', 'pardon'])
    @commands.has_permissions(kick_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                jarg = ['pardoned', 'restored', 'unbaned']
                await ctx.send(f"{user.mention} {random.choice(jarg)}")
                return
   

def setup(bot):
    bot.add_cog(Admin(bot))