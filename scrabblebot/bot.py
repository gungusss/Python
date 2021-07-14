import discord
import os

client = discord.Client()

line1 = ":red_square::white_large_square::white_large_square::blue_circle::white_large_square::white_large_square::white_large_square::red_square::white_large_square::white_large_square::white_large_square::blue_circle::white_large_square::white_large_square::red_square:."
line2 = ":white_large_square::red_circle::white_large_square::white_large_square::white_large_square::blue_square::white_large_square::white_large_square::white_large_square::blue_square::white_large_square::white_large_square::white_large_square::red_circle::white_large_square:."
line3 = ":white_large_square::white_large_square::red_circle::white_large_square::white_large_square::white_large_square::blue_circle::white_large_square::blue_circle::white_large_square::white_large_square::white_large_square::red_circle::white_large_square::white_large_square:."
line4 = ":blue_circle::white_large_square::white_large_square::red_circle::white_large_square::white_large_square::white_large_square::blue_circle::white_large_square::white_large_square::white_large_square::red_circle::white_large_square::white_large_square::blue_circle:."
line5 = ":white_large_square::white_large_square::white_large_square::white_large_square::red_circle::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::red_circle::white_large_square::white_large_square::white_large_square::white_large_square:."
line6 = ":white_large_square::blue_square::white_large_square::white_large_square::white_large_square::blue_square::white_large_square::white_large_square::white_large_square::blue_square::white_large_square::white_large_square::white_large_square::blue_square::white_large_square:."
line7 = ":white_large_square::white_large_square::blue_circle::white_large_square::white_large_square::white_large_square::blue_circle::white_large_square::blue_circle::white_large_square::white_large_square::white_large_square::blue_circle::white_large_square::white_large_square:."
line8 = ":red_square::white_large_square::white_large_square::blue_circle::white_large_square::white_large_square::white_large_square::star::white_large_square::white_large_square::white_large_square::blue_circle::white_large_square::white_large_square::red_square:."
line9 = ":white_large_square::white_large_square::blue_circle::white_large_square::white_large_square::white_large_square::blue_circle::white_large_square::blue_circle::white_large_square::white_large_square::white_large_square::blue_circle::white_large_square::white_large_square:."
line10 = ":white_large_square::blue_square::white_large_square::white_large_square::white_large_square::blue_square::white_large_square::white_large_square::white_large_square::blue_square::white_large_square::white_large_square::white_large_square::blue_square::white_large_square:."
line11 = ":white_large_square::white_large_square::white_large_square::white_large_square::red_circle::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::red_circle::white_large_square::white_large_square::white_large_square::white_large_square:."
line12 = ":blue_circle::white_large_square::white_large_square::red_circle::white_large_square::white_large_square::white_large_square::blue_circle::white_large_square::white_large_square::white_large_square::red_circle::white_large_square::white_large_square::blue_circle:."
line13 = ":white_large_square::white_large_square::red_circle::white_large_square::white_large_square::white_large_square::blue_circle::white_large_square::blue_circle::white_large_square::white_large_square::white_large_square::red_circle::white_large_square::white_large_square:."
line14 = ":white_large_square::red_circle::white_large_square::white_large_square::white_large_square::blue_square::white_large_square::white_large_square::white_large_square::blue_square::white_large_square::white_large_square::white_large_square::red_circle::white_large_square:."
line15 = ":red_square::white_large_square::white_large_square::blue_circle::white_large_square::white_large_square::white_large_square::red_square::white_large_square::white_large_square::white_large_square::blue_circle::white_large_square::white_large_square::red_square:."

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ping'):
        await message.channel.send(f"**Ping** :{round(client.latency * 1000)}")
    
    if message.content.startswith('!scrabble'):
       await message.channel.send(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}\n{line7}")
       await message.channel.send(f"{line8}")
       await message.channel.send(f"{line9}\n{line10}\n{line11}\n{line12}\n{line13}\n{line14}\n{line15}")

client.run('NzEzNzg2NjI1MTgzODQyMzY1.XslLmA.wUok_afCUEAQ6C5TzIlKbzLVnX4')