import discord
import asyncio
from discord.ext import commands

description = '''A very sexy discord bot that scrapes messages from discord channels and returns statistics/graphs, among other things'''
bot = commands.Bot(command_prefix='!', description=description)
bot.load_extension('cogs.kym')
bot.load_extension('cogs.stats')

@bot.event
async def on_ready():
  print('Logged in as %s' % bot.user.name)
  print(bot.user.id)
  print('------')

@bot.command()
async def ayy(ctx):
  '''lmao'''
  await ctx.send('lmao')

@bot.command()
async def source(ctx):
  '''Links MuffinBot's source code'''
  await ctx.send('https://github.com/Muffinlicious/Discord-Stats-Bot')

@bot.command()
@commands.is_owner()
async def quit(ctx):
  '''Kills my bot, epic style'''
  await bot.logout()

if __name__ == '__main__':
  bot.run('token')
