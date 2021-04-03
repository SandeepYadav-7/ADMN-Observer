from discord.ext import commands
import discord
import random

class Basic(commands.Cog):
  def __inti__(self,bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_command_error(self,ctx,ex):
    await ctx.send("someting is wrong, Please contect the Admin")

  @commands.command()
  async def ping(self,ctx):
    await ctx.send("Pong")

  @commands.Cog.listener()
  async def on_ready():
    print("Bot is Ready, in example")


  @commands.Cog.listener()
  async def on_message(self,message:discord.Message):
    print(message.author)






def setup(bot):
  bot.add_cog(Basic(bot))

