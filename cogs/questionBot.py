import discord
from discord.ext import commands
import random

class QuestionGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Questiongame Cog ready')

    @commands.command(aliases=['que', 'q'])
    async def question(ctx, *, question):
        respones = ['idk bro', 'word?', 'lmao what?']
        await ctx.send(f":question: {question}\n :robot: {random.choices(respones)}")


async def setup(bot):
    await bot.add_cog(QuestionGame(bot))