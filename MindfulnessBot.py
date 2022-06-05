import discord
import os
import asyncio
import creds

from discord import channel
from discord.enums import try_enum


client = discord.Client()
# List of messages
groundme = ["Okay, here's a quick breathing exercise we can try; inhale for 5 seconds as slowly and deeply as you can, exhale for 5 seconds (or 6 if you'd prefer) as slowly and deeply as you can.", 
             "Now keep that rhythm for 5 minutes, I'll be here to keep count and remind you to continue your practice until the 5 minutes is up",
             "If you're good, feel free to say !stop to cease the exercise.",
             "I'll let you know when we're done.",
             "Great, you've completed your breathing exercise, take a moment to see how you feel and really go deep with it; how is your mind currently? How is your heartrate? How does your body feel? How do you feel overall?",
             "Take note of that and continue to practice to increase the positive results of this exercise", 
             "Consider yourself grounded, bud!"]
@client.event
async def on_ready():
    print('We have logged in as as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!groundme'):
        task = asyncio.create_task(ground_me(message))
    if message.content.startswith('!stop'):
        await message.channel.send(groundme[6])
        task.cancel()

async def ground_me(message):
    
    await message.channel.send(groundme[0])
    await asyncio.sleep(4)
    await message.channel.send(groundme[1])
    await asyncio.sleep(3)
    await message.channel.send(groundme[2])
    await asyncio.sleep(5)
    await message.channel.send(groundme[3])
    await asyncio.sleep(300)
    await message.channel.send(groundme[4])
    await message.channel.send(groundme[5])

client.run(creds.TOKEN)

