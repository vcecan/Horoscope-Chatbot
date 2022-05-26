import discord
import random
import os
from chatbot_horoscope import  get_message_response
from request import horoscopes
token = 'OTc0MDEzMjY3OTg5MTE0OTYw.GF8Muu.cUiP4njfoCV19H41yl60kJ5Hmtdn8X_TDXidqQ'

client = discord.Client()

@client.event
async  def on_ready():
    print("We have logged in as {0.user}".format(client))



@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    #♎ ♈ ♍ ♉ ♊ ♋ ♌ ♏ ♐ ♑ ♒ ♓
    if message.content=='♈':
        user_message ='aries'
    elif message.content == '♉':
        user_message = 'taurus'
    elif message.content == '♊':
        user_message = 'gemini'
    elif message.content == '♋':
        user_message = 'cancer'
    elif message.content == '♌':
        user_message = 'leo'
    elif message.content == '♍':
        user_message = 'virgo'
    elif message.content == '♎':
        user_message = 'libra'
    elif message.content == '♏':
        user_message = 'scorpius'
    elif message.content == '♐':
        user_message = 'sagittarius'
    elif message.content == '♑':
        user_message = 'capricornus'
    elif message.content == '♒':
        user_message = 'aquarius'
    elif message.content == '♓':
        user_message = 'pisces'
    else:
        user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}:{user_message}({channel}')

    if message.author == client.user:
        return
    if message.channel.name =='horoscope':

        if user_message:
            await message.channel.send(get_message_response(user_message.lower()))
            return

client.run(token)





client.run(os.getenv('TOKEN'))