import discord
from discord.ext import commands
import requests
def dic(word):
  return requests.get(F"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}").json()

class Command(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def help(self, ctx):
    desc = [
      "d!help - Show this embed",
      "d!define <word> - Define a word",
      "d!synonyms <word> - Get synonyms of a word"
    ]
    embed = discord.Embed(
      title = "Dictionary Commands",
      description = "\n".join(desc),
      colour = discord.Colour.blurple()
    )
    embed.url = 'https://impassivemoon03.github.io/discord-bots/dictionary'
    await ctx.send(embed=embed)

  @commands.command(aliases = ['define'])
  async def definition(self, ctx, wd:str = "Yes"):
    word = dic(wd)
    if type(word) == dict:
      return await ctx.send('No word found!')
    word = word[0]
    desc = [
      F"**{word['phonetics'][0]['text']}**"
    ]
    for i in word['meanings']:
      desc.append(F"**{i['partOfSpeech'].capitalize()}**")
      for j in i['definitions']:
        desc.append(j['definition'])
        if('example' in j.keys()):
          desc.append("")
          desc.append(F"Sentence - *{j['example']}*")
          desc.append("-------")
        else:
          desc.append("-------")
    embed = discord.Embed(
      title = F"{word['word'].capitalize()}",
      description = "\n".join(desc),
      colour = discord.Colour.blurple()
    )
    await ctx.send(embed=embed)
  
  @commands.command()
  async def synonyms(self, ctx, wd:str = "Yes"):
    word = dic(wd)
    if type(word) == dict:
      return await ctx.send('No word found!')
    word = word[0]
    desc = []
    for i in word['meanings']:
      for j in i['definitions']:
        if 'synonyms' in j.keys():
          for k in j['synonyms']:
            desc.append(k)
    if len(desc) == 0:
      return await ctx.send('This word does not have synonyms')
    else:
      embed = discord.Embed(
        title = F"{word['word'].capitalize()} Synonyms",
        description = ", ".join(desc),
        colour = discord.Colour.blurple()
      )
      await ctx.send(embed=embed)
  
def setup(client):
  client.add_cog(Command(client))