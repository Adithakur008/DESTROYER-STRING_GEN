from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="⦿ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⦿", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("⦿ sᴜᴘᴘᴏʀᴛ ⦿", url="https://t.me/Friends_Chatting_Masti_Group"),
                    InlineKeyboardButton("⦿ ᴜᴘᴅᴀᴛᴇ ⦿", url="https://t.me/PROFESSOR_NETWORK")
                ],
                [
                    InlineKeyboardButton("⦿ ʀᴇᴘᴏ ⦿", url="https://t.me/PrivateBotRepo"),
                    InlineKeyboardButton("⦿ ᴘʀᴏғᴇssᴏʀ ⦿", url="https://t.me/II_PROFESSOR_SOURABH_II"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
