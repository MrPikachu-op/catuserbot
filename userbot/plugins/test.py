from telethon import events

@tgbot.on(events.NewMessage(pattern="\!hello"))
async def _(event):
    await event.reply("hi fellow cat")
