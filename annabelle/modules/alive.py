from config import MY_ID
from annabelle.helper_funcs.strings import ALIVE_TXT
from annabelle import Annabelle 
from pyrogram import filters as vrn

DEFAULT_IMG = "https://telegra.ph/file/0cf9d9cea0eebd03f6c1e.jpg"
@Annabelle.on_message(vrn.command('alive', HANDLER))
async def alive(Annabelle, message):
     if message.from_user.id == MY_ID:
         await message.reply_photo(photo=DEFAULT_IMG,
                                   caption=ALIVE_TXT.
              )
