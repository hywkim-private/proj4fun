import discord


class Token:
    tok = "NzI0MjEzNzY3MjEwMjcwNzQz.Xu8_jw.ZRs1g1ZMfo1NS4lWmp - SDPv2yNU"


client = discord.client()
client.run(Token.tok)


@client.event
async def on_ready():
    print('logged-in successfully')


@client.event
async def on_message(message):
    id_ = client.get_guild(724228427502190592)
    channels_ = ["commands"]
    if str(message.channel) in channels_:
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
        #elif message.content=="!users":
            #await message.channel.send(f"number of members: {channels.}")



    
client.run(Token.tok)
