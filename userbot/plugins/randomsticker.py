import random
from os import remove
from random import choice
from urllib import parse
import nekos
import requests
from telethon import events, functions, types, utils
import requests
from PIL import Image
from ..utils import admin_cmd , sudo_cmd

BASE_URL = "https://headp.at/pats/{}"
PAT_IMAGE = "pat.webp"

@borg.on(admin_cmd(pattern="cat$"))
@borg.on(sudo_cmd(pattern="cat$", allow_sudo=True))
async def _(event):
    try:
        await event.delete()
    except BaseException:
        pass
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.cat()).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    img.seek(0)
    await event.client.send_file(event.chat_id, open("temp.webp", "rb"), reply_to=reply_to_id)
    remove("temp.webp")
    

#credit to @r4v4n4
#     
def choser(cmd, pack, blacklist={}):
    docs = None

    @borg.on(admin_cmd(pattern="{cmd}$", outgoing=True))
    @borg.on(sudo_cmd(pattern="{cmd}$", allow_sudo=True))
    async def handler(event):
        try:
            await event.delete()
        except BaseException:
            pass
        nonlocal docs
        if docs is None:
            docs = [
                utils.get_input_document(x)
                for x in (
                    await borg(
                        functions.messages.GetStickerSetRequest(
                            types.InputStickerSetShortName(pack)
                        )
                    )
                ).documents
                if x.id not in blacklist
            ]
        await event.respond(file=random.choice(docs))


choser("brain", "supermind")
choser(
    "dab",
    "DabOnHaters",
    {
        1653974154589768377,
        1653974154589768312,
        1653974154589767857,
        1653974154589768311,
        1653974154589767816,
        1653974154589767939,
        1653974154589767944,
        1653974154589767912,
        1653974154589767911,
        1653974154589767910,
        1653974154589767909,
        1653974154589767863,
        1653974154589767852,
        1653974154589768677,
    },
)

# HeadPat Module for Userbot (http://headp.at)
# cmd:- .pat username or reply to msg
# By:- git: jaskaranSM tg: @Zero_cool7870


@borg.on(admin_cmd(pattern="pat$", outgoing=True))
@borg.on(sudo_cmd(pattern="pat$", allow_sudo=True))
async def lastfm(event):
    try:
        await event.delete()
    except BaseException:
        pass
    resp = requests.get("http://headp.at/js/pats.json")
    pats = resp.json()
    pat = BASE_URL.format(parse.quote(choice(pats)))
    with open(PAT_IMAGE, "wb") as f:
        f.write(requests.get(pat).content)
    await event.client.send_file(event.chat_id, PAT_IMAGE, reply_to=event.reply_to_msg_id)
    remove(PAT_IMAGE)
