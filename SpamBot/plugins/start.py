
import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from SpamBot import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID, OWNER_NAME

DOLL_IMG = ALIVE_PIC if ALIVE_PIC else "https://graph.org/file/086e9b9fc0ef2403c2691.png"


Button = [
        [
        Button.url("𝗖𝗵𝗮𝗻𝗻𝗲𝗹", "https://t.me/Bonten_Destroyers"),
        Button.url("𝗦𝘂𝗽𝗽𝗼𝗿𝘁", "https://t.me/Xd_Bots_Support")
        ],
        [
#        Button.url("• Rᴇᴘᴏ •", "https://github.com/KingXdOp/AnonymousSpamBot")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[Xotic](https://t.me/Xotic69"
        DOLL_ON = f"""
**ʜᴇʟʟᴏ {mention},
☞ ᴛʜɪs ɪs ᴛʜᴜɴᴅᴇʀ sᴘᴀᴍʙᴏᴛ!
☞ ᴀ ᴠᴇʀʏ ᴘᴏᴡᴇʀғᴜʟʟ sᴘᴀᴍʙᴏᴛ

**ᴄᴏᴅᴇ ᴄʀᴇᴀᴛᴏʀ** :- {creator}
**[ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ʙᴏᴛ](t.me/{OWNER_NAME} **

✘ ɪғ ʏᴏᴜ ɢᴏᴛ ᴀɴʏ ɪssᴜᴇ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴏᴜʀ [sᴜᴘᴘᴏʀᴛ](t.me/Xd_Bots_Support) ᴀɴᴅ ᴄʜᴀɴɴᴇʟ!**
    """
        await e.client.send_file(e.chat_id, DOLL_IMG, caption=DOLL_ON, buttons=Button)
