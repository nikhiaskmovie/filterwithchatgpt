from pyrogram import Client, filters
from info import CHANNELS
from database.ia_filterdb import save_file

caption_filter =  filters.caption | filters.text

@Client.on_message(filters.chat(CHANNELS) & caption_filter)
async def text(bot, message):
    """Media Handler"""
    for file_type in ("text", "caption"):
        media = getattr(message, file_type, None)
        if media is not None:
            break
    else:
        return

    media.file_type = file_type
    media.caption = message.caption
    await save_file(media)
