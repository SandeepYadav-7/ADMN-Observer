from discord.ext import commands
import discord
import random

def mod_and_owner():
  def pradicate(ctx):
    return commands.check_any(commands.is_owner(),commands.has_role("Moderator"))
  return commands.check(pradicate)


class Admin(commands.Cog):
  def __inti__(self,bot):
    self.bot = bot




  @commands.command()
  @mod_and_owner()
  @commands.has_permissions(manage_messages=True)
  async def clear(self,ctx,amount: int):
    await ctx.channel.purge(limit=amount+1)
  """
  @clear.error()
  async def clear_error(self,ctx,error):
    if isinstance(error,commands.MissingRequiredArgumnet):
      embed = discord.embed(color=discord.Color.red,discraption="Please specity the number of message to delete!")
      await ctx.send(embed,embed)

  """





  









def setup(bot):
  bot.add_cog(Admin(bot))

