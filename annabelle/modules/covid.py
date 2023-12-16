import os
import requests
from requests.utils import requote_uri
from pyrogram import filters as vrn
from config import HANDLER
from Anabelle import Annabelle

API = "https://api.sumanjay.cf/covid/?country="

@Annabelle.on_message(vrn.command("covid", HANDLER))
async def reply_info(client, message):
    query = message.text.split(None, 1)[1]
    await message.edit(
        text=covid_info(query),
        disable_web_page_preview=True,
        quote=True,
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""
**♻️ Covid 19 Information**
**🌐 Country :** `{country}`
**🎭 Actived :** `{active}`
**✅ Confirmed :** `{confirmed}`
**⚰️ Deaths :** `{deaths}`
**🆔 ID :** `{info_id}`
**🚨 Last Update :** `{last_update}`
**⚓ Latitude :** `{latitude}`
**🗼 Longitude :** `{longitude}`
**🎙️ Recovered :** `{recovered}`
"""
        return covid_info
    except Exception as error:
        return error

