import os
from discord.ext import commands
import discord
import asyncio
import configparser
import random

# Read config
config = configparser.ConfigParser()
config.read('config.ini')

prefix = ['$ ']
bot = commands.Bot(command_prefix=prefix, description='Erik\'s selfbot', pm_help=None, self_bot=True)


@bot.event
async def on_ready():
    print('{} has started.'.format(bot.user.name))
    print('------')

    await bot.change_presence(status=discord.Status.online, game=discord.Game(name='github.com/ErikBoesen'))


@bot.event
async def on_message(message):

    await bot.wait_until_ready()
    await bot.wait_until_login()
    #print('Recieved message in #%s from %s.' % (message.channel.name, message.author.nick))

"""
async def name_rotate(bot):
    pass

bot.loop.create_task(name_rotate(bot))
"""

bot.run(config['main']['token'], bot=False)
