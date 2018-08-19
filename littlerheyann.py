# LittleRheyann v1.1 ©2018 Rheylogic - LowfatEnvelope
# ONLY works with Python 3.6. 3.7 has an unspecified error with Discord.py and asyncio.
import discord

TOKEN = 'heh'

client = discord.Client()

#Inital stuff
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hey there, {0.author.mention}!'.format(message)
        await client.send_message(message.channel, msg)

#Check.
    if message.content.startswith('!test'):
        msg = 'All is well, {0.author.mention}!'.format(message)
        await client.send_message(message.channel, msg)

#Online Status
@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('I am Online!')
    print('Awaiting commands.')

client.run(TOKEN)