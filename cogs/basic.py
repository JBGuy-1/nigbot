from discord.ext import commands
import discord

class Basic(commands.Cog):
    def __init(self, bot):
        self.bot = bot

    @commands.command()
    async def heya(self,ctx):
        await ctx.send("sup boye")

    @commands.command()
    async def embed(self, ctx):
        my_fav_color = discord.colour.Color.from_rgb(123, 109, 114)
        myembed = discord.Embed(title="embed title",color=my_fav_color).set_author(name="hangar bot")
        await ctx.send(embed=myembed)
    

def setup(bot):
    bot.add_cog(Basic(bot))


