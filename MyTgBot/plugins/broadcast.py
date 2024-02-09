from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid
from MyTgBot import mongodb, bot
from pyrogram import filters
from pyrogram.types import *
from pyrogram import enums
import asyncio, datetime, time

db = mongodb["BROADCAST"]

@bot.on_message(filters.command(["broadcast", "users"]))  
async def users(c, m):
    if m.text == "/users":
        total_users = db.count_documents({})
        return await m.reply(f"Total Users: {total_users}")
    b_msg = m.reply_to_message
    sts = m.reply_text("Broadcasting your messages...")
    users = db.find({})
    total_users = db.count_documents({})
    done = 0
    failed = 0
    success = 0
    start_time = time.time()
    async def broadcast(c, m):
        user_id = int(user['id'])
        try:
            await b_msg.copy(chat_id=user_id)
            success += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await b_msg.copy(chat_id=user_id)
            success += 1
        except InputUserDeactivated:
            await db.delete_many({'id': user_id})
            failed += 1
        except UserIsBlocked:
            failed += 1
        except PeerIdInvalid:
            await db.delete_many({'id': user_id})
            failed += 1
        except Exception as e:
            failed += 1
        done += 1
        if not done % 20:
            await sts.edit(f"Broadcast in progress:\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nFailed: {failed}")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await m.delete()
    await message.reply_text(f"Broadcast Completed:\nCompleted in {time_taken} seconds.\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nFailed: {failed}", quote=True)
