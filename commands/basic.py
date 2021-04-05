from discord.ext import commands
import discord
import random
import time
import datetime
import asyncio

class Basic(commands.Cog):
  def __inti__(self,bot):
    self.bot = bot
  
 


  



  @commands.Cog.listener()
  async def on_message(self,message:discord.Message):
    
    if message.content == '<@!827810245890932756>':
      embed = discord.Embed(title="ADMN Ovserver",description="My prefix is = \nYou can also use ADMN and A! prefix for using me",color = discord.Color.dark_purple())

      embed.set_thumbnail(url=message.author.avatar_url)
      embed.set_footer(text=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),icon_url=message.author.avatar_url)

      await message.channel.send(embed=embed)


"""
 @commands.Cog.listener()
  async def on_command_error(self,ctx,ex):
    await ctx.send("someting is wrong, Please contect the Admin")
"""






def setup(bot):
  bot.add_cog(Basic(bot))

'''

'''