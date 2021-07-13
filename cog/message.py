import requests
import discord
from discord.ext import commands
def dic(word):
  return requests.get(F"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}").json()

class Message(commands.Cog):
  def __intit__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.bot: 
      return
    if str(message.channel.type) == 'private':
      word = dic(message.content)
      if type(word) == dict:
        return await message.channel.send('No word found!')
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
      await message.channel.send(embed=embed)

def setup(client):
  client.add_cog(Message(client))