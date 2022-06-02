import discord
import os
from dotenv import load_dotenv
from tabulate import tabulate
from functions import list_fights, fetch, refresh_list
import aiocron
from datetime import datetime

load_dotenv()
client = discord.Client()

@aiocron.crontab('0 1 * * *')
async def cronjob():
    fetch()
    data = list_fights()
    dates = data[0][1].split(" ")
    now = datetime.now().strftime("%d %b").split(" ")
    if ((dates[1] == now[1]) and (dates[2] == now[0])):
        channel = client.get_channel(int(os.getenv('CHANNEL_ID')))
        roleid = os.getenv('ROLE_ID')
        await channel.send(f'<@&{roleid}> {data[0][0]}' + ' today @ ' + f'{data[0][2]}')

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
