import discord
from discord.ext import commands
import random

class QuestionGame(commands.Cog):
    def __init__(self, bot):
        self.bot - bot


    @commands.command(aliases=['que', 'q'])
    async def question(ctx, *, question):
        respones = ['idk bro', 'word?', 'lmao what?']
        await ctx.send(f":question: {question}\n :robot: {random.choices(respones)}")


def setup(bot):
    bot.add_cog(QuestionGame(bot))