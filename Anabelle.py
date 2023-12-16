from pyrogram import Client, __version__
from config import *
import logging
from os import path, mkdir
from sys import stdout
from datetime import datetime
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger

LOG_DATETIME = datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
LOGDIR = f"{__name__}/logs"

if not path.isdir(LOGDIR):
    mkdir(LOGDIR)

LOGFILE = f"{LOGDIR}/{__name__}_{LOG_DATETIME}_log.txt"

file_handler = FileHandler(filename=LOGFILE)
stdout_handler = StreamHandler(stdout)

basicConfig(
    format="%(asctime)s - [Annabelle] - %(levelname)s - %(message)s",
    level=INFO,
    handlers=[file_handler, stdout_handler],
)

getLogger("pyrogram").setLevel(WARNING)
logger = getLogger(__name__)

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



app = Annabellee()
app.run()
