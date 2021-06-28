import json
import discord
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
        await message.channel.send('Hello!')
    if msg.startswith('$help'):
        await message.channel.send(HELP_COMMAND)
    if msg.startswith("$build"):
        url = 'https://poebuildroulette.github.io/#'
        webbrowser.open(url)
        await message.channel.send("xd")
    if msg.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)


# client.run(os.getenv('TOKEN'))
client.run('ODU4NjAwMTA2MzY2NTk5MTY5.YNgfqQ.mZzbbBTXO0CiCeBVze2cAPoa4DI')
