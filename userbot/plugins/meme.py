import asyncio

from .. import CMD_HELP
from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(outgoing=True, pattern="^\:/$"))
@bot.on(sudo_cmd(pattern="^\:/$", allow_sudo=True))
async def kek(keks):
    keks = await edit_or_reply(keks , ":\\")
    uio = ["/", "\\"]
    for i in range(1, 15):
        await asyncio.sleep(0.3)
        txt = ":" + uio[i % 2]
        await keks.edit(txt)


@bot.on(admin_cmd(outgoing=True, pattern="^\-_-$"))
@bot.on(sudo_cmd(pattern="^\-_-$", allow_sudo=True))
async def lol(lel):
    lel = await edit_or_reply(lel , "--")
    okay = "-_-"
    for _ in range(10):
        await asyncio.sleep(0.3)
        okay = okay[:-1] + "_-"
        await lel.edit(okay)


@bot.on(admin_cmd(outgoing=True, pattern="^\;_;$"))
@bot.on(sudo_cmd(pattern="^\;_;$", allow_sudo=True))
async def fun(e):
    e = await edit_or_reply(e,";;")
    t = ";__;"
    for _ in range(10):
        await asyncio.sleep(0.3)
        t = t[:-1] + "_;"
        await e.edit(t)


@bot.on(admin_cmd(outgoing=True, pattern="oof$"))
@bot.on(sudo_cmd(pattern="oof$", allow_sudo=True))
async def Oof(e):
    t = "Oof"
    catevent = await edit_or_reply(e, t)
    for _ in range(15):
        await asyncio.sleep(0.3)
        t = t[:-1] + "of"
        await catevent.edit(t)


@bot.on(admin_cmd(outgoing=True, pattern="type (.*)"))
@bot.on(sudo_cmd(pattern="type (.*)", allow_sudo=True))
async def typewriter(typew):
    message = typew.pattern_match.group(1)
    sleep_time = 0.2
    typing_symbol = "|"
    old_text = ""
    typew = await edit_or_reply(typew, typing_symbol)
    await asyncio.sleep(sleep_time)
    for character in message:
        old_text = old_text + "" + character
        typing_text = old_text + "" + typing_symbol
        await typew.edit(typing_text)
        await asyncio.sleep(sleep_time)
        await typew.edit(old_text)
        await asyncio.sleep(sleep_time)


@bot.on(admin_cmd(pattern=f"meme", outgoing=True))
@bot.on(sudo_cmd(pattern=f"meme", allow_sudo=True))
async def meme(event):
    memeVar = event.text
    sleepValue = 0.5
    memeVar = memeVar[6:]
    if not memeVar:
        memeVar = "✈️"
    event = await edit_or_reply(event, "-------------" + memeVar)
    await asyncio.sleep(sleepValue)
    await event.edit("------------" + memeVar + "-")
    await asyncio.sleep(sleepValue)
    await event.edit("-----------" + memeVar + "--")
    await asyncio.sleep(sleepValue)
    await event.edit("----------" + memeVar + "---")
    await asyncio.sleep(sleepValue)
    await event.edit("---------" + memeVar + "----")
    await asyncio.sleep(sleepValue)
    await event.edit("--------" + memeVar + "-----")
    await asyncio.sleep(sleepValue)
    await event.edit("-------" + memeVar + "------")
    await asyncio.sleep(sleepValue)
    await event.edit("------" + memeVar + "-------")
    await asyncio.sleep(sleepValue)
    await event.edit("-----" + memeVar + "--------")
    await asyncio.sleep(sleepValue)
    await event.edit("----" + memeVar + "---------")
    await asyncio.sleep(sleepValue)
    await event.edit("---" + memeVar + "----------")
    await asyncio.sleep(sleepValue)
    await event.edit("--" + memeVar + "-----------")
    await asyncio.sleep(sleepValue)
    await event.edit("-" + memeVar + "------------")
    await asyncio.sleep(sleepValue)
    await event.edit(memeVar + "-------------")
    await asyncio.sleep(sleepValue)
    await event.edit("-------------" + memeVar)
    await asyncio.sleep(sleepValue)
    await event.edit("------------" + memeVar + "-")
    await asyncio.sleep(sleepValue)
    await event.edit("-----------" + memeVar + "--")
    await asyncio.sleep(sleepValue)
    await event.edit("----------" + memeVar + "---")
    await asyncio.sleep(sleepValue)
    await event.edit("---------" + memeVar + "----")
    await asyncio.sleep(sleepValue)
    await event.edit("--------" + memeVar + "-----")
    await asyncio.sleep(sleepValue)
    await event.edit("-------" + memeVar + "------")
    await asyncio.sleep(sleepValue)
    await event.edit("------" + memeVar + "-------")
    await asyncio.sleep(sleepValue)
    await event.edit("-----" + memeVar + "--------")
    await asyncio.sleep(sleepValue)
    await event.edit("----" + memeVar + "---------")
    await asyncio.sleep(sleepValue)
    await event.edit("---" + memeVar + "----------")
    await asyncio.sleep(sleepValue)
    await event.edit("--" + memeVar + "-----------")
    await asyncio.sleep(sleepValue)
    await event.edit("-" + memeVar + "------------")
    await asyncio.sleep(sleepValue)
    await event.edit(memeVar + "-------------")
    await asyncio.sleep(sleepValue)
    await event.edit(memeVar)


@bot.on(admin_cmd(pattern=f"give", outgoing=True))
@bot.on(sudo_cmd(pattern=f"give", allow_sudo=True))
async def give(event):
    if event.fwd_from:
        return
    giveVar = event.text
    sleepValue = 0.5
    lp = giveVar[6:]
    if not lp:
        lp = " 🍭"
    event = await edit_or_reply(event, lp + "        ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + "       ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + "      ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + "     ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + "    ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + "   ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + "  ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + " ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + lp)
    await asyncio.sleep(sleepValue)
    await event.edit(lp + "        ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + "       ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + "      ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + "     ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + "    ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + "   ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + "  ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + " ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + lp)


CMD_HELP.update(
    {
        "meme": "**Plugin : **`meme`\
        \n\n**Commands :**\
        \n  •  `:/`\
        \n  •  `-_-`\
        \n  •  `;_;`\
        \n  •  `.oof`\
        \n\n**Functions :**\
        \n__The above four commands are animation commands__\
        \n\n**Commands :**\
        \n  •  `.meme`\
        \n  •  `.give`\
        \n\n**Functions :**\
        \n__The above two commands are animation memes meme by default takes ✈️ and give by default takes 🍭__\
        \n\n**Syntax :** `.type`\
        \n**Usage : **Just a small command to make your keyboard become a typewriter!\
        "
    }
)
