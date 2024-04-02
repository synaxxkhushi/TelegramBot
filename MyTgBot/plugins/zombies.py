from pyrogram import filters
from MyTgBot import bot

@bot.on_message(filters.command("cleanzombies"))
async def ban_deleted_accounts(_, m):
    chat_id = m.chat.id
    deleted_users = []
    banned_users = 0
    m = await m.reply("Finding ghosts...")

    async for i in app.get_chat_members(chat_id):
        if i.user.is_deleted:
            deleted_users.append(i.user.id)
    if len(deleted_users) > 0:
        for deleted_user in deleted_users:
            try:
                await m.chat.ban_member(deleted_user)
            except Exception:
                pass
            banned_users += 1
        await m.edit(f"Banned {banned_users} Deleted Accounts")
    else:
        await m.edit("There are no deleted accounts in this chat")
