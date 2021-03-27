from discord.ext import commands
from celestai import settings, brain

global msg

def run():
    client = commands.Bot(command_prefix = settings.WAKE_UP_EXTENSION)

    @client.event
    async def on_message(message):

        if not message.content:
            log.info('No text input received.')

        msg = message

        brain.inst.match_mods(message.content)
        brain.inst.execute_mods(message.content)

        def send(phrase):
            message.channel.send(phrase)

        #await message.channel.send(tts.discordphrase)

    



    client.run('ODE1MzcwMjg0MzUzMDYwODc1.YDrawA.5nJMqFaCIpl68-fFOx1nguI3DXU')


