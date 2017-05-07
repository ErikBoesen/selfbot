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
    try:
        print('Recieved message in #%s from %s.' % (message.channel.name, message.author.nick))
    except AttributeError:
        print('Recieved message in #%s from %s.' % (message.channel.name, message.author.name))


async def spam(bot):
    await bot.wait_until_ready()

    while not bot.is_closed:
        print('Sending message in #spam180...')
        msg = await bot.send_message(bot.get_channel('176515260516139009'), get_random_string())
        await asyncio.sleep(59)
        await bot.delete_message(msg)


def get_random_string():
    return random.choice(['!levels', '!rank', '%%tba team %s' % random.randint(0, 6200)])


bot.loop.create_task(spam(bot))
bot.run(config['main']['token'], bot=False)
