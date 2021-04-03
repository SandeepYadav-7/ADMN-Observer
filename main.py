from alive import keep_alive
from discord.ext import commands
import os


bot = commands.Bot(description="Still Development",strip_after_prefix=True,command_prefix=["A!","ADMN","-"],case_insensitive=True)

for filename in os.listdir("./commands"):
  if filename.endswith(".py") and filename != "__init__.py":
    bot.load_extension(f'commands.{filename[:-3]}')

keep_alive()
bot.run(os.getenv("TOKEN"))