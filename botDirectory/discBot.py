import json
import discord
from discord.ext import commands
import os
import requests
import webbrowser


client = discord.Client()
HELP_COMMAND = "List of Commands:$hello, $build, $inspire\n" + "$hello: returns a hello message(why not?)\n" + \
               "$build: redirects to random poe build page. Have fun :)\n" + "$inspire: generates a random inspirational quote."


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return (quote)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if msg.startswith('$hello'):
        await message.delete()
        await message.channel.send('Hello!')
    if msg.startswith('$help'):
        await message.delete()
        await message.channel.send(HELP_COMMAND)
    if msg.startswith("$build"):
        await message.delete()
        url = 'https://poebuildroulette.github.io/#'
        webbrowser.open(url)
        await message.channel.send("xd")
    if msg.startswith("$gay"):
        await message.delete()
        send = 'minng loves boys'
        await message.channel.send(send)
    if msg.startswith("$inspire"):
        await message.delete()
        quote = get_quote()
        await message.channel.send(quote)
    if msg.startswith("$booba"):
        await message.delete()
        await message.channel.send('https://tenor.com/view/booba-gif-19163211')
    if msg.startswith("$xd"):
        await message.delete()
        await message.channel.send('https://tenor.com/view/pepe-laugh-he-doesnt-know-pepe-gif-14019260')


# client.run(os.getenv('TOKEN'))
client.run('')
