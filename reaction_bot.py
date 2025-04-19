import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji

api_id = 28782604
api_hash = 'e5a1c0ee714544244e25b2a9d3e06e69'
bot_token = '7812109263:AAHMB2MMu9ysJvPD9o7Rg44RtbbNo2Jb5k0'
channel_username = '@rasulovshokh'

client = TelegramClient('reaction_bot', api_id, api_hash).start(bot_token=bot_token)

reactions = ['💋']

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    print("✅ Yangi post kelib tushdi!")  # Debug
    await asyncio.sleep(60)
    for emoji in reactions:
        try:
            await client(SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                reaction=[ReactionEmoji(emoticon=emoji)]
            ))
            print(f"➡️ {emoji} bosildi")
            await asyncio.sleep(1)
        except Exception as e:
            print(f"⚠️ Xatolik: {e}")

print("🤖 Bot tayyor. Post kutmoqda...")
client.run_until_disconnected()
