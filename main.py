from datetime import datetime
from distutils import extension
from email import message
from lib2to3.pgen2 import token
import random
from sqlite3 import Timestamp
from turtle import clear, color
import discord
from discord.ext import commands
import os
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
for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.{fn[:-3]}")
# load


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send("loaded")

# unload


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send("unloaded cog")

# reload


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    await ctx.send("reloaded cog")


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


@bot.command(aliases=['que', 'q'])
async def question(ctx, *, question):
    respones = ['idk bro', 'word?', 'lmao what?']
    await ctx.send(f":question: {question}\n :robot: {random.choices(respones)}")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked")

# ban


@bot.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    # if (not ctx.author.guild_permissions.manage_messages):
    #   await ctx.send('nice try. reserved for mods only')
    #   return
    await member.ban(reason=reason)
    await ctx.send(f"RIP bozo!\n{member.mention} has been banned")

# Unban


@bot.command(aliases=['forgive', 'vindicate', 'pardon'])
@commands.has_permissions(kick_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            jarg = ['pardoned', 'restored', 'unbaned']
            await ctx.send(f"{user.mention} {random.choice(jarg)}")
            return

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
@bot.command(aliases=['av', 'pfp', 'dp'])
async def avatar(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    memberav = member.avatar_url
    avembed = discord.Embed(title=f"{member.name}\'s pfp")
    avembed.set_image(url=memberav)

    await ctx.send(embed=avembed)

# keep_alive()


key = os.environ.get("BOT_TOKEN")
bot.run(key)

# verify 953710369996685342
# main chat 953583957579026444
