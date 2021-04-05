from discord.ext import commands
import discord
import random
import time
import datetime
import asyncio

class info(commands.Cog):
  def __inti__(self,bot):
    self.bot = bot



  



  @commands.command()
  async def userinfo(self,ctx,*,member:discord.Member = None):
    
    def format_time(timee):
      return timee.strftime("%d-%B-%Y, %H:%M:%S")

    member = member if member else ctx.author

    embed = discord.Embed(title="%s INFO: "%member.name,color=discord.Color.dark_purple())
    embed.add_field(name="ID",value=member.id)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Created At:-",value=format_time(member.created_at))
    embed.add_field(name="joined At:-",value=format_time(member.joined_at))

    sorted_roles = sorted([role for role in member.roles[1:]],key=lambda x: x.position)
    embed.add_field(name="Roles",value=", ".join(role.mention for role in sorted_roles),inline=False)
    await ctx.send(embed=embed)









def setup(bot):
  bot.add_cog(info(bot))

'''

  @commands.Cog.listener()
  async def on_command_error(self,ctx,ex):
    await ctx.send("someting is wrong, Please contect the Admin")
'''