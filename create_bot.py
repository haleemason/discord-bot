# imports
import discord
import os
from prices import crypto_parser
from dotenv import load_dotenv
from discord.ext import commands

# Credentials
load_dotenv('.env')

# Create bot
client = commands.Bot(command_prefix='!')


# Startup info
@client.event
async def on_ready():
    print('connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


# Command
@client.command()
async def helloworld(ctx):
    await ctx.send('Hello World!')


@client.command()
async def goodbyeworld(ctx):
    await ctx.send('Goodbye forever')


@client.command()
async def gene(ctx):
        symbol = 'GENE'
        price, percent_change_1h = crypto_parser(symbol=symbol)
        name = f"{symbol}: ${price} ({percent_change_1h}%)"
        await ctx.send(f"{symbol}:  ${price}  ({percent_change_1h})")


# Run the bot
client.run(os.getenv('SIFF_BOT_TOKEN'))