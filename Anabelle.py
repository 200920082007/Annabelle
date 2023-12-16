from pyrogram import Client, __version__
from config import *
import logging

art = """

   _____                      ___.          .__  .__          
  /  _  \   ____   ____ _____ \_ |__   ____ |  | |  |   ____  
 /  /_\  \ /    \ /    \\__  \ | __ \_/ __ \|  | |  | _/ __ \ 
/    |    \   |  \   |  \/ __ \| \_\ \  ___/|  |_|  |_\  ___/ 
\____|__  /___|  /___|  (____  /___  /\___  >____/____/\___  >
        \/     \/     \/     \/    \/     \/               \/ 


"""

Annabellee = Client(name="Annabelle", api_id=API_ID, api_hash=API_HASH,
              session_string=SESSION_STRING, plugins={"root": "annabelle/modules"})

