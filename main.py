from discord.ext import commands
import os

client = commands.Bot(command_prefix = "d!")
client.remove_command('help')

@client.event
async def on_ready():
  print('Logged In')

client.load_extension('cog.commands')
client.load_extension('cog.message')

client.run(os.environ.get('TOKEN'))