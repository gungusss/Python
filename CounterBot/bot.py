import discord
import os

client = discord.Client()

ChannelID = 852971541749825556

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ping'):
        await message.channel.send(f"**Ping** :{round(client.latency * 1000)}")
    
    if message.content.startswith('!counter start'):
        if message.channel.id == ChannelID:
            await message.channel.send("Please start with the number 1")
            for i in range(100):
                if message.content == i:
                    print("Nice")
                else:
                    print("not nice")
        else:
            print("nope")
       

client.run('NzEzNzg2NjI1MTgzODQyMzY1.XslLmA.wUok_afCUEAQ6C5TzIlKbzLVnX4')