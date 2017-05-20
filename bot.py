from discord.ext import commands
import discord
import asyncio
import re

from yaml import load


# Read config
with open('config.yaml', 'r') as f:
    config = load(f)

bot = commands.Bot(command_prefix=['$ '], description='Erik\'s selfbot', pm_help=None, self_bot=True)


@bot.event
async def on_ready():
    print('{} has started.'.format(bot.user.name))
    print('------')


@bot.event
async def on_message(message):

    await bot.wait_until_ready()
    await bot.wait_until_login()

    """Catch a user's messages and figure out what to return."""
    # Use regex to match the command at the starting of a
    # TODO: Figure out how to match this directly without substringing.
    try:
        cmd = re.search(r'^\$ (\w+)', message.content).group(0)[2:]
        content = message.content[len(cmd)+3:]  # The 3 is for the '$ ' and the space after the command.
    except AttributeError:
        cmd = None
        content = None

    # Only send back message if user that sent the triggering message isn't a bot
    if message.author == bot.user and cmd is not None:
        print('Recieved command %s.' % cmd)
        if cmd == 'prune':
            # TODO: Prune a given number of messages in the channel where the request was sent
            pass


async def game_rotate(bot):
    """
    Switch game regularly between configured list of phrases.

    These phrases do not actually have to be games.
    """
    await bot.wait_until_ready()

    while not bot.is_closed:
        for game in config['games']:
            print('Changing game: %s' % game)
            await bot.change_presence(status=discord.Status.online, game=discord.Game(name=game))
            await asyncio.sleep(59)


if config['custom_game']:
    bot.loop.create_task(game_rotate(bot))

bot.run(config['token'], bot=False)
