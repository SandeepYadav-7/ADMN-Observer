from discord.ext.commands import Cog
from discord.ext import commands
import math
import re
import json
from discord import Embed
import discord



class test(Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_redy(self):
    print(f"{self._class__.__name__} Cog has been loaded\n....")

  @commands.command(name="help",aliases=["h","commands"],description="The help command")
  async def help(self,ctx,cog="1"):
    helpEmbed = discord.Embed(title="Help commands!",color=discord.Color.dark_purple())
    helpEmbed.set_thumbnail(url=ctx.author.avatar_url)

    #get a list of all our current cogs & remove ones without commands
    cogs = [c for c in self.bot.cogs.keys()]
    cogs.remove("Basic")

    totalPages = math.ceil(len(cogs)/4)


    if re.search(r"\d",str(cog)):
      cog = int(cog)
      if cog > totalPages or cog < 1:
        await ctx.senf(f"Invalid page number: `{cog}`. Please pick from {totalPages} pages. \nAlternatively, Simply run `help` to see page one or type `help` [category] to see that  categories help commands!")
        return 

      helpEmbed.set_footer(text=f"<> Required & [] - Optional | Page {cog} of {totalPages}")
      neededCogs = []
      for i in range(4):
        x = i +(int(cog)-1)*4
        try:
          neededCogs.append(cogs[x])
        except IndexError:
          pass
      for cog in neededCogs:
        commandList = ""
        for command in self.bot.get_cog(cog).walk_commands():
          if command.hidden:
            continue
          elif command.parent != None:
            continue
          if command.description == "":
            commandList += f"**{command.name}** - *NO description*\n"
          else:
            commandList += f"**{command.name}** - *{command.description}*\n"
        commandList += "\n"
        helpEmbed.add_field(name=cog,value=commandList,inline=False)

    elif re.search(r"[a-zA-Z]",str(cog)):
      lowerCogs = [c.lower() for c in cogs]
      if cog.lower() not in lowerCogs:
        await ctx.send(f"Invalid argument: `{cog}` Please pick from {totalPages} pages.\nAlternatively, Simply run `help` to see page one or type `help` [category] to see that  categories help commands!")
        return

      helpEmbed.set_footer(text=f"<> = Required & [] = Optional | Cog {(lowerCogs.index(cog.lower())+1)} of {len(lowerCogs)}")

      helpText = ""
      for command in self.bot.get_cog(cogs[lowerCogs.index(cog.lower())]).walk_commands():
        
        if command.hidden:
          continue
        elif command.parent != None:
          continue
        if command.description == "":
          helpText += f"```{command.name}```\n**No Description**\n\n"
        else:
          helpText += f"```{command.name}```\n**{command.description}**\n\n"


        if len(command.aliases) > 0:
          helpText += f"**Aliases: ** `{', '.join(command.aliases)}`\n"
        
        helpText += '\n'
        
        with open(r"resource/prefixs.json","r") as f:
          prefixes = json.load(f)
        try:
          prefix = prefixes[str(ctx.guild.id)]
        except KeyError:
          prefix = prefixes[str(ctx.guild.id)]
          prefix = "$"

        helpText += f'**format:** ` {prefix} {command.name} {command.usage if command.usage is not None else ""}`\n\n'
      
      helpEmbed.description = helpText
    else:
      await ctx.send(f"1Invalid argument: `{cog}`\nPlease pick form {totalPages} pages.\nAlternatively, Simply run `help` to see page one or type `help` [category] to see that  categories help commands!")
      return
    await ctx.send(embed=helpEmbed)
        




"""

def syntax(command):
  cmd_and_aliases = "|".join([str(command),*command.aliases])
  params = []
  for key,value in command.params.items():
    if key not in ("self","ctx"):
      params.append(f"[{key}]" if "NoneType" in str(value) else f"<{key}>")

  params = " ".join(params)


  return f"`{cmd_and_aliases} {params}`"

#example!alias <reuired> [optional]


class HelpMenu(ListPageSource):
  def __init__(self,ctx,data):
    self.ctx == ctx

    super().__init__(data,per_page=3)

  async def write_page(self,menu,fields=[]):
    offset = (menu.current_page*self.per_page) + 1
    len_data = len(self.entries)
    embed = Embed(title="Help",description="Welcome to the ADMN help dialog!",color=discord.Color.dark_purple())
    #embed.set_thumbnail(url=self.ctx.guild.me.avater_url)
    embed.set_footer(text=f"{offset:,} - {min(len_data,offset+self.per_page - 1):,} of {len_data:,} command.")

    for name,value in fields:
      embed.add_filds(name=name,value=value,inline=False)
    return self.write_page(menu,fields)
    
    
  async def format_page(self,menu,entries):
    fields = []
    for entry in entries:
      fields.append((entry.brief or "No description",syntax(entry)))
    return await self.write_page(menu,fields)




class Help(Cog):
  def __init__(self,bot):
    self.bot=bot
    self.bot.remove_command("help")

  async def cmd_help(self,ctx,command):
    embed = Embed(title=f"Help with `{command}`",description=syntax(command),color=discord.Color.dark_purple())

    embed.add_field(name="Command description",value=command.help)
    await ctx.send(embed=embed)


  @command(name="help")
  async def show_help(self,ctx,cmd: Optional[str]):
    
    if cmd is None:
      menu = MenuPages(source=HelpMenu(ctx,list(self.bot.commands)),clear_reactions_after=True,delete_message_after=True,timeout=60.)
      await menu.start(ctx)
    else:
      if (command := get(self.bot.commands,name=cmd)):
        await self.cmd_help(ctx,command)
    if cmd in None:
      pass
    else:
      if (command := get(self.bot.comands,name=cmd)):
        await self.cmd_help(ctx,command)

"""

"""
  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_reday.reday_up("help")
"""


def setup(bot):
  bot.add_cog(test(bot))