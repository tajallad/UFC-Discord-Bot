import discord
import os
from dotenv import load_dotenv
from tabulate import tabulate
from functions import list_fights, fetch, refresh_list
#import aiocron

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!fetch'):
        updates = fetch()
        await message.channel.send(f'UFC data fetched, {updates} new events added.')
    
    if message.content.startswith('!events'):
        fight_list = list_fights()
        tabulated = tabulate(fight_list, headers=["Main Event", "Date", "Time", "Card"])
        await message.channel.send("```" + tabulated + "```")
    
    if message.content.startswith('!refresh'):
        refresh_list()
        await message.channel.send(f'Event data refreshed.')


client.run(os.getenv('TOKEN'))