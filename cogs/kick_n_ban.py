import discord
from discord.ext import commands
import random

class Kicks(commands.Cog):
    def __init__ (self, bot):
        self.bot=bot

    ## kick member
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked")


    ## ban member
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def ban(self,ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"RIP bozo!\n{member.mention} has been banned")

    ## unban menber
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
    bot.add_cog(Kicks(bot))