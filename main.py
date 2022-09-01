import os
import random
from datetime import datetime
from distutils import extension
from email import message
from sqlite3 import Timestamp
from turtle import clear, color
import asyncio

import discord
from discord.ext import commands
from sympy import limit

#from keep_alive import keep_alive
#my_secret = os.environ['token']

prefix = "-"
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.event
async def on_ready():
    print(f"The {bot.user} bot is online!")

# cogs
async def load_cog():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
    
            # cut off the .py from the file name



@bot.command()
async def hi(ctx):
    await ctx.send("heya, its your friendly neighborhood hangar bot!")


@bot.event
async def on_member_join(member):
    colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000,
              0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
    # Welcome message channel id
    wlc_channel = bot.get_channel(953593435695251506)

    # Role we want to add automatically
    embed = discord.Embed(title=f"Welcome {member.name}!", color=random.choice(
        colors)).set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.add_field(name="Thank you for joining the server!",
                    value=f"You gotta check <#953710369996685342> to verify your acc before getting full access to the server\nCan't wait to meet you in <#953583957579026444> ", inline=True)
    embed.set_footer(icon_url=f"{member.guild.icon_url}",
                     text=f"You are member number {member.guild.member_count}!")
    await wlc_channel.send(embed=embed)
    await wlc_channel.send(f"{member.mention}")


@bot.event
async def on_raw_reaction_add(payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, bot.guilds)

    if payload.emoji.name == "😎" and payload.message_id == 964930101290610778:
        role = discord.utils.get(guild.roles, name="homies")
        if role is not None:
            member = discord.utils.find(
                lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
# Remove roles


@bot.event
async def on_raw_reaction_remove(payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, bot.guilds)

    if payload.emoji.name == "😎" and payload.message_id == 964930101290610778:
        role = discord.utils.get(guild.roles, name="homies")
        if role is not None:
            member = discord.utils.find(
                lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)


@bot.command()
async def verify(ctx):
    verify_embed = discord.Embed(
        title="Welcome to the hangar!").set_author(name="")
    verify_embed.add_field(name="let's get you started",
                           value=f"Click the 😎 emoji to get full access to this server ")
    verify_embed.set_footer(text=f"")

    react_messasge = await ctx.send(embed=verify_embed)
    await react_messasge.add_reaction(emoji="😎")


# error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"lmao, that's reserved for mods")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('missing required arguments')
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send('Member does not exist')


# server stats

# Show Avatar

# keep_alive()


key = os.environ.get('BOT_TOKEN')

async def main():
    await load_cog()
    await bot.start(key)
# bot.run(key)

asyncio.run(main())


# verify 953710369996685342
# main chat 953583957579026444