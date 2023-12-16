import logging
from config import MY_ID, HANDLER
from annabelle.helper_funcs.strings import ALIVE_TXT
from pyrogram import filters
from Anabelle import Annabelle

DEFAULT_IMG = "https://telegra.ph/file/0cf9d9cea0eebd03f6c1e.jpg"


@Annabelle.on_message(filters.command('alive', HANDLER))
async def alive_command_handler(client, message):
    """
    Command handler for the 'alive' command.
    Replies with a photo and caption.
    """
    if message.from_user.id == MY_ID:
        try:
            await message.reply_photo(
                photo=DEFAULT_IMG,
                caption=ALIVE_TXT
            )
            logger.info("Alive message sent successfully.")
        except Exception as e:
            # Log the exception
            logger.error(f"Error sending alive message: {str(e)}")
            
            # Handle exceptions if photo sending fails
            await message.reply_text(f"Error sending alive message: {str(e)}")
