from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""
👹💫 යක්ක🇱🇰අඩවිය™ (Group Music Bot) 💫👹
Telegram UserBot to Play Audio in Telegram Voice Chats 🔊

**All Users**
/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly

**Admins only**
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/userbotleave - remove assistant from your chat
/admincache - Refresh admin list

©2021 @YakkaAdaviyaMusicBot Bot All Rights Reserved
""",
        reply_markup=InlineKeyboardMarkup(
            [
                    [
                        InlineKeyboardButton(
                             text=" 👪 Bot Support Group ",
                             url="https://t.me/sltechzoneofficial"),
                         InlineKeyboardButton(
                             text=" 🔔 Bot Update Channel ",
                             url="https://t.me/sltechzone")
                    ],
                    [
                        InlineKeyboardButton(
                             text=" 👺 Yakka Adaviya Group ",
                             url="https://t.me/yakkaadaviyaofficial"),
                         InlineKeyboardButton(
                             text=" 👹 Yakka Adaviya Channel ",
                             url="https://t.me/yakkaadaviya")
                    ],
                    [
                        InlineKeyboardButton(
                            text=" ⚡️ Developer ",
                             url="https://t.me/hirunaofficial") 
                    
                    ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""
        👹💫 යක්ක🇱🇰අඩවිය™ (Group Music Bot) 💫👹\n\nTelegram UserBot to Play Audio in Telegram Voice Chats 🔊\n\n©2021 @YakkaAdaviyaMusicBot Bot All Rights Reserved
        """,
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "️Start Bot", url="https://t.me/YakkaAdaviyaMusicBot")
                ]
            ]
        )
   )