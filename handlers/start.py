from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""
        👹💫 යක්ක🇱🇰අඩවිය™ (Group Music Bot) 💫👹
        
        Telegram UserBot to Play Audio in Telegram Voice Chats 🔊
        
        ©2021 @YakkaAdaviyaMusicBot Bot All Rights Reserved
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                    [
                        InlineKeyboardButton(
                             text=" 👪 Support Group ",
                             url="https://t.me/sltechzoneofficial"),
                         InlineKeyboardButton(
                             text=" 🔔 Update Channel ",
                             url="https://t.me/sltechzone")
                    ],
                    [
                        InlineKeyboardButton(
                            text=" 🙋 Help ",
                            url="https://t.me/dewmibot?start=help"),
                         InlineKeyboardButton(
                            text=" ⚡️ Developer ",
                             url="https://t.me/hirunaofficial")        
                       
                    ],
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""
        👹💫 යක්ක🇱🇰අඩවිය™ (Group Music Bot) 💫👹
        
        Telegram UserBot to Play Audio in Telegram Voice Chats 🔊
        
        ©2021 @YakkaAdaviyaMusicBot Bot All Rights Reserved
        """,
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "️Start", url="https://t.me/YakkaAdaviyaMusicBot")
                ]
            ]
        )
   )