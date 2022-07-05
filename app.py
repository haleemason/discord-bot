import asyncio
import os

from discord.ext import commands
from dotenv import load_dotenv

import discord
from get_price import crypto_parser

# Credentials, take, as environment variables from .env file
load_dotenv(".env")

# Create bot
client = commands.Bot(command_prefix="!")

# Startup info
@client.event
async def on_ready():
    print("connected to bot: {}".format(client.user.name))
    print("Bot ID: {}".format(client.user.id))


@client.command()
async def gene(ctx):
    """
    Command to get the current price of GENE token and the change in price over the last 1 hour.

    :param ctx: Discord context
    :return: Returns
    """
    symbol = "GENE"
    price, percent_change_1h = crypto_parser(symbol=symbol)
    name = f"{symbol}: ${price} ({percent_change_1h}%)"
    await ctx.send(name)


async def gene_price() -> None:
    """
    Monitors the current price of GENE token and the change in price over the last 1 hour.
    Updates every 5 seconds.
    :return: None
    """
    await client.wait_until_ready()
    symbol = "GENE"
    price, percent_change_1h = crypto_parser(symbol=symbol)
    name = f"${round(price,1)} {percent_change_1h}"

    print(name)
    while not client.is_closed():
        await client.change_presence(activity=discord.Activity(name=name, type=discord.ActivityType.watching))
        await asyncio.sleep(5)


client.loop.create_task(gene_price())


if __name__ == "__main__":
    # Run the bot
    client.run(os.getenv('DISCORD_CLIENT_SECRET'))
    activity = discord.Activity(type=discord.ActivityType.watching, name="!help")
    bot = commands.Bot(command_prefix="!", activity=activity, status=discord.Status.idle)
