#Flanke Discord Bot Coded BY Zemo[BotDEV]


#____________________________________________#
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from random import randint
from discord.voice_client import VoiceClient
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
status = ['Use', 'The', 'Prefix', ';']
startup_extensions = ["Music"]
bot = commands.Bot(command_prefix=';') #This will be the prefix for your bot
bot.remove_command("help")

class Main_Commands():
        def _init_(self, bot):
         self.bot = bot

#____________________________________________#
async def change_status():
    await bot.wait_until_ready()
    msgs = cycle(status)

    while not bot.is_closed:
        current_status = next(msgs)
        await bot.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(5)

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
async def equip(ctx):
    await bot.say("***Keyboard***\nRazer Blackwidow\n***Mouse***\nRazer Death Adder\n***Microphone***\nSnowball Mic\n***Mods***\nBadlion Client")




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
    embed.add_field(name="Suggest <What you would like to suggest>", value="Send a suggestion to what Flanke should do.", inline=True)
    embed.add_field(name="Warn", value="Warn a user.", inline=True)
    embed.add_field(name="Kick", value="Kick a user.", inline=True)
    embed.add_field(name="Ban", value="Ban a user.", inline=True)
    embed.add_field(name="Purge", value="Clears a certain amount of messages that are defined.", inline=True)
    embed.add_field(name="Report", value="Report a user if they do break the rules.", inline=True)
    embed.add_field(name="Equip", value="States the equipment Flanke uses.", inline=True)
    await bot.send_message(author, embed=embed) #This will message the author that typed .help

#____________________________________________#
@bot.event
async def on_message(message):
    chat_filter = ["faggot", "nigga", "hoe", "N.igger", "n_i_G_G_E_R", "Ni.gger", "nig.ger", "nigg.er", "retard", "nigger", "kys"]
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


@bot.command(pass_context=True)
async def report(ctx,reported:discord.Member, *, message):
    message=f'***Reportee:***\n{ctx.message.author.mention}\n***Reporting:***\n{reported.mention}\n ***Reason For Report:***\n*{message}*'
    await bot.send_message(bot.get_channel("489134651970027541"), message)



#____________________________________________#
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    rant = random.randint(1, 255)
    if ctx.message.author.server_permissions.kick_members:
        embed = discord.Embed(title="{}'s info".format(user.name), description="Heres what I could find on {}!", color=rant)
        embed.add_field(name="Name", value=user.name, inline=True) #Gives the username without the @ and #
        embed.add_field(name="ID", value=user.id, inline=True) #Give id of the user you tagged
        embed.add_field(name="Status", value=user.status, inline=True) #Gives status of the user. online, dnd, offline, etc.
        embed.add_field(name="Highest role", value=user.top_role) #Tells you the highest role of that user.
        embed.add_field(name="Joined", value=user.joined_at) #Give you the date and time the user joined.
        await bot.say(embed=embed)
    else:
        await bot.say("No Permission")


@bot.command(pass_context=True)
async def server(ctx):
    if ctx.message.author.server_permissions.kick_members:    
        embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Heres what i got!.", color=0x00FFC9)
        embed.set_author(name="Flake's Public Discord")
        embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
        embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
        embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
        embed.add_field(name="Members", value=len(ctx.message.server.members))
        await bot.say(embed=embed)
    else:
        await bot.say("No Permission!")

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
        await bot.say("No Perms!")



@bot.command(pass_context=True)
async def suggest(ctx,*,  bugs: str):
    emb_3_1 = discord.Embed(title="{} has suggested".format(ctx.message.author), value=bugs , color=0x0072ff)
    emb_3_1.add_field(name="Suggestion: ", value=bugs)
    emb_3_1.set_footer(text="Thanks for the suggestion {}! ".format(ctx.message.author))
    await bot.send_message(bot.get_channel("488852504164171786"), embed=emb_3_1)
    

#Mute---------#

@bot.command(pass_context = True)
async def mute(ctx, user: discord.Member,*,  bugs: str):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '417445689249890304':
        embed = discord.Embed(title="{} has been muted!".format(user.name), value=bugs , color=0x0072ff)
        role = discord.utils.get(user.server.roles, name="Muted")
        await bot.add_roles(user, role)
        embed.add_field(name="Reason For Mute: ", value=bugs)
        await bot.send_message(bot.get_channel("489876538909655051"), embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)
#Ban----------#
@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.kick_members:
        embed = discord.Embed(title="{} has been banned!".format(user.name), description="You will need to unban {} when ready!!!".format(user.name) , color=0x0072ff)
        embed.set_footer(text="Next time. Follow the rules.")
        embed.set_thumbnail(url=user.avatar_url)
        await bot.ban(user)
        await bot.say(embed=embed)
    else:
       embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff0000)
       embed.set_footer(text="Sorry.")
       await bot.say(embed=embed)       


#Kick-------#
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    rant = random.randint(1, 255)
    if ctx.message.author.server_permissions.kick_members:
        embed = discord.Embed(title="{} has been kicked!".format(user.name), description="Next time is a ban {}!!".format(user.name), color=rant)
        embed.set_footer(text="Next time. Follow the rules.")
        embed.set_thumbnail(url=user.avatar_url)
        await bot.kick(user)
        await bot.say(embed=embed)
    else:
       embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=rant)
       embed.set_footer(text="Sorry.")
       await bot.say(embed=embed)       

#Warn--------#
@bot.command(pass_context=True)
async def warn(ctx, user: discord.Member,*,  bugs: str):
    emb_3_1 =discord.Embed(title="Warned: {} ".format(user.name))
    emb_3_1.add_field(name="Reason Warned: ",value=bugs)
    emb_3_1.set_thumbnail(url=ctx.message.author.avatar_url)
    await bot.send_message(bot.get_channel("489876538909655051"),embed=emb_3_1)
#-----------------TESTING------------------------------#
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extention {}\n{}'.format(extension, exc))

#____________________________________________#
bot.loop.create_task(change_status())
bot.run('NDg1Nzg0MjM4Mjc3MjYzMzYy.Dm1lbA.4j4rWqdxBeVee63rkt3y0hWxA3w')
