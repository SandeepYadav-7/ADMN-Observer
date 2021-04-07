from discord.ext import commands
import discord
import json

def mod_and_owner():
  def pradicate(ctx):
    return commands.check_any(commands.is_owner(),commands.has_role("Moderator"))
  return commands.check(pradicate)

class Prefix(commands.Cog):
  def __inti__(self,bot):
    self.bot = bot

  @commands.command(description="setprefix <new prefix>",name='setprefix',breif="set prefix for me",aliases=["setp","sp"],brief="To set a prefix")
  @mod_and_owner()
  async def setprefix(self,ctx,*,prefix):
    with open(r"resource/prefixs.json","r") as f:
      prefixes = json.load(f)

      prefixes[str(ctx.guild.id)] = prefix
      

      with open("resource/prefixs.json","w") as f:
        json.dump(prefixes,f,indent=4)

      embed = discord.Embed(color=discord.Color.green(),description=f"`{prefix}` is the new guild prefix")

      await ctx.send(embed=embed)

  @setprefix.error
  async def setprefix_handler(self, ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
      embed = discord.Embed(color=discord.Color.red(),description="you forgot to give me input please give me a input")
      await ctx.send(embed=embed)


  @commands.command(description="to get the current prefix",name='getprefix',breif="get may current prefix for this guild",aliases=["gp","getp"],brief="To get a prefix")
  async def getprefix(self,ctx):
    with open(r"resource/prefixs.json","r") as f:
      prefixes = json.load(f)

    prefix = prefixes[str(ctx.guild.id)]

    embed = discord.Embed(color=discord.Color.green(),description=f"`{prefix}` is your guild current prefix")

    await ctx.send(embed=embed)

       

        

  
  
 


  







def setup(bot):
  bot.add_cog(Prefix(bot))

