# Import necessary libraries
import os
import discord
from dotenv import load_dotenv
from vocab import Vocab
from time import sleep
from helpers import Helpers
from actioner import Actionner
import json

vocab = Vocab('vocabulary')
actionner = Actionner()

# specify the token that alerts hafid
call_token = 'hafid'
baliz = ""

# Load evironment from .env and retrieve token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Create hafid client
hafid = discord.Client()

#usefull functions

# normalize given string
def normalize(msg):
    result = msg
    normalization_data = json.loads(Helpers("normalization.json").readFile())
    tokens = msg.split(' ')
    for token in tokens:
        if token in dict(normalization_data).keys() :
            if " "+token+" " in result :
                result = result.replace(" "+token+" ", " "+normalization_data[token]+" ")
            elif " "+token in result:
                result = result.replace(" "+token, " "+normalization_data[token]+" ")
            elif result.startswith(token+" "):
                result = result.replace(token+" ", normalization_data[token]+" ")
            else: pass
    return result

# delete successive duplicated letters
def dedupeLetters(msg):
    result = ""
    token = msg[0]
    for l in msg:
        if l != token :
            result += token
            token = l
    return result + msg[len(msg)-1]

@hafid.event
async def on_ready():
    print(f'{hafid.user} is now connected to Discord!')

@hafid.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, ' + vocab.get('message.welcome') + " hhh, dkhal m3ana l server douz l buvet o khod kass atay"
    )

@hafid.event
async def on_message(message):
    global baliz
    # Skip if its the same user or client not mentioned
    msg = normalize(dedupeLetters(message.content.lower()))
    if message.author == hafid.user : return

    print(message.content)

    if call_token not in msg and baliz == "" : return

    if actionner.handle(msg) != False : response = actionner.getResponse()
    else :
        if call_token == msg: response = vocab.get('message.welcome', True)
        elif 'menu' in msg : response = vocab.get('message.menu')
        elif 'thanks' in msg or 'thank you' in msg : response = vocab.get('message.thanks', True).format(message.author.name)
        elif 'baliz' in msg :
            response = vocab.get('message.baliz', True)
            if baliz == "" : baliz = msg
        else : response = vocab.process(msg)

        if response == 'K' :
            await message.channel.send(response)
            response = vocab.process(baliz)
            baliz = ""

    # replace variable tokens & ch letters
    response = response.replace("[name]", message.author.name)
    
    await message.channel.send(response)

print("Connecting hafid to discord...")
hafid.run(token)