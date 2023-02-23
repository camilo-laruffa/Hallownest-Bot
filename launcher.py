from library.bot import bot
import emoji

VERSION = "0.0.2"

@bot.event
async def on_message(message):
    if message.channel.id != 884182152881799238:
        print("Mensaje de " + str(message.author) + ": " + str(message.content))
        return

    if message.author == bot.user:
        return
    

    if "TOMAS" in message.content.upper():    
        await message.channel.send("JAJAJ tomas truco")
        return    

    await message.add_reaction(emoji.emojize(':rolling_on_the_floor_laughing:'))
    await message.add_reaction(emoji.emojize(':neutral_face:'))
    await message.add_reaction(emoji.emojize(':worried_face:'))
    


bot.run(VERSION)