from pyrogram import filters
from pyrogram.types import Message

from Mickey import OWNER, App
from Mickey.databash import get_served_chats, get_served_users


@App.on_message(filters.command("stats") & filters.user(OWNER))
async def get_stats(_, msg: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await msg.reply_photo(
        photo="https://te.legra.ph/file/2d5b054acddf865d4d83e.png",
        caption=f"ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {BOT_NAME}\n\n➻ **ᴄʜᴀᴛs :** {chats}\n➻ **ᴜsᴇʀs :** {users}",
    )
