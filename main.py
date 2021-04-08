from alive import keep_alive
from discord.ext import commands
import json
import os
import discord
intents = discord.Intents.default()
intents.members = True


def get_prefix(bot, message):
	if not message.guild:
		return commands.when_mentioned_or("$")(bot, message)

	with open("resource/prefixs.json", "r") as f:
		prefixes = json.load(f)
	if str(message.guild.id) not in prefixes:
		return commands.when_mentioned_or("$")(bot, message)
	prefix = prefixes[str(message.guild.id)]
	return commands.when_mentioned_or(prefix)(bot, message)


bot = commands.Bot(description="Still Development",
                   strip_after_prefix=True,
                   command_prefix=get_prefix,
                   case_insensitive=True,
                   help_command=None,
                   intents=intents)

for filename in os.listdir("./commands"):
	if filename.endswith(".py") and filename != "__init__.py":
		bot.load_extension(f'commands.{filename[:-3]}')

keep_alive()
bot.run(os.getenv("TOKEN"))
