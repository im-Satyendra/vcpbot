from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 

@Client.on_message(filters.command("a"))
async def s(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**add me in group and make me admin and  use /v as a reply to video\n/s to stop**",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "contact me", url="t.me/a_l_satya")
                                    ]]
                            ))
   else:
      await m.reply("**i know /v /s only ✨**")
