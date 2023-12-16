import asyncio
from pyrogram import Client, filters
from annabelle.modules.helpmenu.help_menu import modules_help
from config import HANDLER

@Client.on_message(
    filters.command(["leave", "lc"], prefixes=f"{HANDLER}") & filters.me
)
async def leave_chat(client: Client, message):
    chat = message.chat.type
    chat_id = message.chat.id
    if chat in ["group", "supergroup"]:
        await message.edit("My Master Doesn't Like This Chat, Leaving Bye...")
        await asyncio.sleep(3)
        await client.leave_chat(chat_id)
    else:
        await message.edit("This chat is not in group or supergroup")

modules_help.append(
    {"leave": [{"leave" or "lc": "Leaves chat"}]}
)

# Most of the codes are simple because of time limitation.
# There will be more features pushed through updates.
