from discord.ext import commands
from discord import File
import discord
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
  def __inti__(self,bot):
    self.bot = bot
  
  @commands.command()
  async def card(self,ctx,member:discord.Member=None):
    if not member:
      member = ctx.author

    
    
    asset = member.avatar_url_as(size=128)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((1400,1400))
    wel = Image.open("861297.jpg")
    d1 = ImageDraw.Draw(wel)
    myFont = ImageFont.truetype('text.ttf', 240)
    d1.text((800, 1600), "Welcome to ADMN",font=myFont, fill=(68,0,102))
    d1.text((1600, 1850),ctx.author.name,font=myFont, fill=(68,0,102))
    
    #wel.paste(pfp,(489,1169))
    #wel.text((10,10), "Hello World", fill=(255,255,0))

    
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
    #wel.save("wel.jpg")
    await ctx.send(file= discord.File("wel.jpg"))
    os.remove("wel.jpg")



  

def setup(bot):
  bot.add_cog(Basic(bot))
