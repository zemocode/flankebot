#Flanke Discord Bot Coded BY Zemo[BotDEV]


#____________________________________________#
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from random import randint
import random
import asyncio
import pickle
import os
import json
from itertools import cycle
import time
import re
#____________________________________________#

Client = discord.Client()
bot = commands.Bot(command_prefix=';') #This will be the prefix for your bot
bot.remove_command("help")

#____________________________________________#
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Bot Is Online')
#____________________________________________#
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Member')
    await bot.add_roles(member, role)


#____________________________________________#

@bot.command(pass_context=True)
async def help(ctx):
    await bot.say("You Have Been Sent Help In Your Messages!")    
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='Help') #This will be the title of the WHOLE ENTIRE message.
    embed.add_field(name="Links", value="Give you Flankes links.", inline=True)
    await bot.send_message(author, embed=embed) #This will message the author that typed .help

#____________________________________________#
@bot.event
async def on_message(message):
    chat_filter = ["faggot", "nigga", "hoe", "N.igger", "n_i_G_G_E_R", "Ni.gger", "nig.ger", "nigg.er", "fucking", "retard", "nigger"]
    bypass_filter = []
    contents = message.content.split(" ")
    for word in contents:
        if word.lower() in chat_filter:
            if not message.author.id in bypass_filter:
                try:
                    await bot.delete_message(message)
                    await bot.send_message(message.channel, "You can't say that, Sorry!")
                except discord.errors.NotFound:
                    return
    await bot.process_commands(message)
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content.lower())
    if url and message.channel.id == "405815888177266689":
             await bot.delete_message(message)
             await bot.say("Say that in #advertisment!")
#____________________________________________#
@bot.command(pass_context=True)
async def links(ctx):
    await bot.say('**Youtube**\nhttps://www.youtube.com/channel/UCJs2lYkiApLerCx1VqZyi7Q\n**Twitter**\nhttps://twitter.com/FlankeVEVO\n**Pack**\nhttps://www.mediafire.com/file/9oa714v59787397/§3+Misty+32x.zip\n***End of links***')

#____________________________________________#
@bot.command(pass_context = True)
async def purge(ctx, number):
    if ctx.message.author.server_permissions.kick_members:
        mgs = [] #Empty list to put all the messages in the log
        number = int(number) #Converting the amount of messages to delete to an integer
        async for x in bot.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        await bot.delete_messages(mgs)
    else:
        await bot.say("No Permissions")


#____________________________________________#
bot.run('BOT_TOKEN')
