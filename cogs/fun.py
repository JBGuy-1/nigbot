import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    ## show pfp
    @commands.command(aliases=['av','dp','pfp'])
    async def avatar(self,ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        memberav = member.avatar_url
        avembed = discord.Embed(title=f"{member.name}\'s pfp")
        avembed.set_image(url=memberav)

        await ctx.send(embed=avembed)
    


    
async def setup(bot):
    await bot.add_cog(Fun(bot))