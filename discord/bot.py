import discord


class Token:
    tok = NzI0MjEzNzY3MjEwMjcwNzQz.Xu8_jw.ZRs1g1ZMfo1NS4lWmp - SDPv2yNU


client = discord.client()
client.run(Token.tok)


@client.event
async def on_ready():
    print('logged-in successfully')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(Token.tok)
