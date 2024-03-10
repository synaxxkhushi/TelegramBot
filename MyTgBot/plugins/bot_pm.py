from pyrogram import filters
from pyrogram.types import Message
from MyTgBot import bot

OWNER_ID = "1666544436"

@bot.on_message(
    filters.private
    & filters.incoming
 )
async def on_pm_s(_, message: Message):
    if not message.from_user.id == 1666544436:
        fwded_mesg = await message.forward(
            chat_id=OWNER_ID,
            disable_notification=True
        )
