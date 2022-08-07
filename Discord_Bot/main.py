from random import random
import discord
import random

TOKEN = "MTAwNTkzMzY4MzgxNzA2MjQ3Mg.Gc57S-.hP-RK_hj0gyCjOYQ0Fl3H-seTk5SWqkHBfEGRk"


client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'username: {username}: {user_message} , channel: {channel}')
    
    
    if message.author == client.user:
        return
    
    if message.channel.name == 'general': 
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}')
            return
        elif user_message.lower() == 'random':
            response = f'this is random number {random.randint(1,100)}'
            await message.channel.send(response)
            return
        
    if user_message.lower() == 'anywhere':
        await message.channel.send(f'{username} is anywhere')
        return

client.run(TOKEN)















