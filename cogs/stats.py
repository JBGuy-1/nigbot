import discord
from discord.ext import commands

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot =  bot
    @commands.command()
    async def severinfo(self,ctx, member:discord.Member=None):
        role_count = len(ctx.guild.roles)
        self.member=ctx.author

        s_stat = discord.Embed(title="Server Stats !", Timestamp=ctx.message.created_at)
        s_stat.add_field(name='Name',value=f"{ctx.guild.name}", inline=True)
        s_stat.add_field(name='Number of users',value=f"{ctx.guild.member_count}", inline=True)
        s_stat.add_field(name='Roles',value=str(role_count), inline=True)
        s_stat.add_field(name="",icon_url= ctx.author.avatar_url)

        await ctx.send(embed=s_stat)

def setup(bot):
    bot.add_cog(Stats(bot))