import json
import requests
from Anabelle import Annabelle
from config import MY_ID, HANDLER
from pyrogram import filters as vrn
from pyrogram.types.messages_and_media import Message


@Annabelle.on_message(vrn.command("github", HANDLER))
async def github(bot:Annabelle, msg:Message) :
    if msg.from_user.id == MY_ID :
        args = msg.text.split(None, 1)
        if len(args) >= 2:
            query = args[1]
            await msg.edit("`searching github...`")
            try :
              get_url = f"https://api.github.com/search/users?q={query}"
              request1 = requests.get(get_url)
              json_data = request1.json()
              raw_data = json_data["items"]
              data_ = raw_data[0]
              url = data_["html_url"]
              request2 = requests.get(url)
              data = request2.json()
              await msg.edit_text(
    text=f"""
<b>__Stdout__</b>
<b>Query</b>: <code>{query}</code>

<b>ID</b>: <code>{data["id"]}</code>
<b>Url</b>: <a href="{url}">ʟɪɴᴋ</a>
<b>Type</b>: <code>{data["type"]}</code>
<b>Name</b>: <code>{data["name"]}</code>
<b>Login</b>: <code>{data["login"]}</code>
<b>Public Repos</b>: <code>{data["public_repos"]}</code>
<b>Following</b>: <code>{data["following"]}</code>
<b>Followers</b>: <code>{data["followers"]}</code>
<b>Email</b>: <code>{data["email"]}</code>

<b>ANABELLE USERBOT</b>
""",
    parse_mode="html"
)
