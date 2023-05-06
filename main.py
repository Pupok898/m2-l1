import discord
intents = discord.Intents.default() intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
your_channel = client.guilds[0].text_channels[0]
await your_channel.send('Мы рекомендуем начать с изучения основных принципов устойчивого развития и экологической ответственности. Это поможет понять, как наши действия влияют на окружающую среду и как мы можем уменьшить свой негативный след.Далее, можно изучить конкретные экологические практики, такие как раздельный сбор мусора, переработка отходов, использование экологически чистых материалов и продуктов, энергосбережение и т.д.')


client.run('MTEwNDM3NjUzMzMzMTc0Njg0Ng.GeqAuk.XmWeaAT8hlZpYyiJrxOkMQBMTVRJEPdtOj3yoM')
