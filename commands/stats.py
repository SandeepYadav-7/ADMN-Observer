from discord.ext import commands
from platform import python_version
from time import time
from discord import __version__ as discord_version
import discord
import random
from datetime import datetime,timedelta
from psutil import Process,virtual_memory

import datetime

class stats(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def test(self,ctx):
    await ctx.send(self.bot)

  @commands.command()
  async def ping(self,ctx):
    
    user = ctx.author
    proc = Process()
    with proc.oneshot():
      uptime = timedelta(seconds=time()-proc.create_time())
    embed = discord.Embed(description="ADMN observer is always alive",color = discord.Color.dark_purple())
    embed.add_field(name="BOT latency",value="%s ms"%round(self.bot.latency * 1000))
    embed.add_field(name="Bot Uptime",value=uptime)
    embed.set_footer(text="Requested by:- "+ctx.author.name+" | "+datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),icon_url=user.avatar_url)

    await ctx.send(embed=embed)


  @commands.command(name="stats")
  async def botinfo(self,ctx):
    embed = discord.Embed(title="Bot stats",color=ctx.author.colour,thumbnail=self.bot.user.avatar_url,timestamp=datetime.datetime.utcnow())
    proc = Process()
    with proc.oneshot():
      uptime = timedelta(seconds=time()-proc.create_time())
      cpu_time = timedelta(seconds=(cpu := proc.cpu_times()).system*cpu.user)
      mem_total = virtual_memory().total /(1024**2)
      mem_of_total = proc.memory_percent()
      mem_usage = mem_total * (mem_of_total /100)

    fields =[
      {"Bot Version",1.0,True},
      {"Python Version",python_version(),True},
      {"Discord.py version",discord_version,True},
      {"Uptime",uptime,True},
      {"CPU time",cpu_time,True},
      {"Memory Usage",mem_total,True},
      {"Users","",True},
      #{"Python Version",self.bot.guild.member_count,True},
    ]
    for name,value,inline in fields:
      embed.add_field(name=name,value=value,inline=inline)

    await ctx.send(embed.embed)
    
    



def setup(bot):
  bot.add_cog(stats(bot))

