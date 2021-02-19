from telethon import TelegramClient, events, sync
from gtts import gTTS
# import os
# import random

api_id = 1101345
api_hash = '053281e3cfcdced232fa20bea4d3fb07'
bot_token = '1508652969:AAFNoL2FlaUpihwVZqImY4VP5VsD4N2RC7g'
tg_group = 's1440763835_15901639657692418142'

client = TelegramClient('slap', api_id, api_hash)
client.start(bot_token=bot_token)

# SLAP action
@client.on(events.NewMessage(pattern='\!slap'))
async def handler(event):
    users = await client.get_participants(tg_group)
    sender = (await event.get_sender()).first_name
    slapped = random.choice(users)

    await event.reply(sender + ' has slapped @' + slapped.username)

# TTS action
"""
@client.on(events.NewMessage(pattern='\!tts (.+)'))
async def handler(event):
    filename = str(int(round(time.time() * 1000))) + '.mp3'
    text = event.pattern_match.group(1)[:50]
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

    await event.reply(file=filename)
    os.remove(filename)
"""

client.run_until_disconnected()
