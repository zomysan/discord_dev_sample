from discord.ext import commands
import config
import asyncio
import discord

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("on_ready")


bot.load_extension("cogs.greet")
bot.run(config.TOKEN)