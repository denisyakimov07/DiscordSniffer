from discord_client import client

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print(message.content)
        await message.channel.send('Hello3!')
        print(message.content)


