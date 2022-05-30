import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.client}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.starswith('!test'):
        await message.channel.send('hello')