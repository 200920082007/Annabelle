from datetime import datetime
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger
from os import path, mkdir
from sys import stdout
from pyrogram import Client
from config import *

# Constants Naming Convention
LOG_DATETIME = datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
LOGDIR = "logs"  

if not path.isdir(LOGDIR):
    mkdir(LOGDIR)

LOGFILE = f"{LOGDIR}/{__name__}_{LOG_DATETIME}_log.txt"

# Imports Order
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
 /  /_\  \ /    \ /    \ \__  \ | __ \_/ __ \|  | |  | _/ __ \ 
/    |    \   |  \   |  \/ __ \| \_\ \  ___/|  |_|  |_\  ___/ 
\____|__  /___|  /___|  (____  /___  /\___  >____/____/\___  >
        \/     \/     \/     \/    \/     \/               \/ 
"""

# Use the Client class to create an instance
Annabelle = Client(
    "Annabelle",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
    plugins={"root": "annabelle/modules"}
)

logger.info(art)

if __name__ == "__main__":
    Annabelle.run()
