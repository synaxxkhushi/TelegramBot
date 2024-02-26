import os
from pyrogram import Client, filters
from pyrogram.types import Message
from MyTgBot import bot
import pyrogram

@bot.on_message(filters.private & filters.command("clone"))
async def bot_clone(bot: bot, msg: Message):
    chat = msg.chat
    cmd = msg.command
    try:
        TOKEN = msg.text.split()[1]
    except IndexError:
        await msg.reply("Please provide a valid BOT_TOKEN.\nUsage:\n\n /clone BOT_TOKEN")
        return

    text = await msg.reply("Booting Your Client")
    
    try:        
        # Change your root directory here
        bot = Client(":memory:", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, plugins={"root": "MyTgBot"})
        await bot.start()
        await pyrogram.idle()
        user = await bot.get_me()
        await text.edit(f"Booted Client as @{user.username} Do /ping Or .ping for testing")        
        await msg.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \n\n Use Help For Help Menu\n\nThanks for Cloning.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
