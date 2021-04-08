import discord
import datetime
import json
from discord.ext import commands
from discord.ext.commands import CommandNotFound , BadArgument,MissingRequiredArgument,MissingPermissions
from discord.errors import Forbidden
import os
from PIL import Image, ImageDraw, ImageFont,ImageFilter,ImageOps,ImageChops
from io import BytesIO


def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result



class Basic(commands.Cog):
  def __init__(self,bot):
    self.bot = bot








  
  @commands.Cog.listener()
  async def on_member_join(self, member):

    role = discord.utils.get(member.guild.roles,name="Member")
    channel = self.bot.get_channel(825452404887257118)
    i_channel = self.bot.get_channel(825548040885895188)
    rule_channel = self.bot.get_channel(825436767263391764)
    role_channel = self.bot.get_channel(825452570960199721)

    embed = discord.Embed(color=discord.Color.dark_purple(),title=f"Welcome to ADMN {member.name}")
    embed.add_field(name="Introduce yourself on",value=i_channel.mention,inline=False)
    embed.add_field(name="Read some Basic Rules from",value=rule_channel.mention,inline=False)
    embed.add_field(name="Don't Forget to select the role from",value=role_channel.mention,inline=False)
    embed.set_footer(text="Learn Together Teach Together")
    embed.set_thumbnail(url=member.avatar_url)



    asset = member.avatar_url_as(size=128)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((1400,1400))
    wel = Image.open("/resource/861297.jpg")
    d1 = ImageDraw.Draw(wel)
    myFont = ImageFont.truetype('resource/text.ttf', 240)
    d1.text((800, 1600), "Welcome to ADMN",font=myFont, fill=(68,0,102))
    d1.text((800, 1850),str(member),font=myFont, fill=(68,0,102))
    
    

    
    im1 = pfp
   
    im2 = wel
    im1 = add_margin(im1,150,0,0,1160,0)


    mask = Image.new("L", im1.size, 128)
    #im1 = Image.composite(im1, im2, mask) 


    mask = Image.new("L", im1.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((1200, 250, 2550,1500), fill=255)
    #im = Image.composite(im1, im2, mask)

    mask_blur = mask.filter(ImageFilter.GaussianBlur(10))
    wel = Image.composite(im1, im2, mask_blur)
  
    wel.save("wel.jpg")

    await member.add_roles(role)
    await channel.send("Hello %s"%member.mention,embed=embed,file= discord.File("wel.jpg"))
    os.remove("wel.jpg")


  



  @commands.Cog.listener()
  async def on_message(self,message:discord.Message):
    if message.content == '<@!827810245890932756>' or message.content == '<@827810245890932756>':
      with open(r"resource/prefixs.json","r") as f:
        prefixes = json.load(f)
      try:
        prefix = prefixes[str(message.guild.id)]

        embed = discord.Embed(title="ADMN Ovserver",description=f"My current prefix for this is `{prefix}` \nYou can also mendtion me as a prifex",color = discord.Color.dark_purple())

      

        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),icon_url=message.author.avatar_url)
      except KeyError:
        prefix = prefixes[str(message.guild.id)]

        embed = discord.Embed(title="ADMN Ovserver",description="My current prefix for this is $ \nYou can also mendtion me as a prifex",color = discord.Color.dark_purple())

      

        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),icon_url=message.author.avatar_url)


      

      await message.channel.send(embed=embed)








def setup(bot):
  bot.add_cog(Basic(bot))

"""
  
  @commands.Cog.listener()
  async def on_command_error(self,ctx,exc):
    if isinstance(exc,CommandNotFound):
      await ctx.send("commands not found Please check the help page",delete_after=5)
    elif isinstance(exc,BadArgument):
      await ctx.send("You didn't provied good argument cheack help argument",delete_after=5)
    elif isinstance(exc,Forbidden):
      await ctx.send("I do not have permission to do that.",delete_after=5)
    elif isinstance(exc,MissingRequiredArgument):
      await ctx.send("you didn't provide the argument",delete_after=5)
    elif isinstance(exc,MissingPermissions):
      await ctx.send("you don't have permission to use this command",delete_after=5)
    else:
      await ctx.send("someting is wrong, Please contect the Admin",delete_after=5)

"""