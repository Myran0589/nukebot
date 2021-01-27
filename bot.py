import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(bot.user.name)
    print('==============')
    print('Made by Myran#0589')
    print('==============')

@bot.command()
async def nuke(ctx, id: int):
    '-nuke channl_id Ex- -nuke 803831591565656104'
    nuke_channel = bot.get_channel(id)
    x = await ctx.send(f"{nuke_channel.name} is nuked successfully !!")
    await asyncio.sleep(2)
    new_channel = await nuke_channel.clone(reason="Nuked!")
    await nuke_channel.delete()
    await new_channel.send("https://cdn.discordapp.com/attachments/774758789396037664/803833762177220639/unnamed.gif")


bot.run("bot token")
