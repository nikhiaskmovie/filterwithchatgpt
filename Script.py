import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

class script(object):
    START_TXT = """<b>Hᴇʏ {} ɪᴍ 『 ᴍᴏᴠɪᴇs ғɪʟᴛᴇʀ ʙᴏᴛ 』 For Only AskAnyMovie.</b>
    
<i>Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ sᴇᴇ ᴛʜᴇ ᴍᴀɢɪᴄ ᴏʀ ʀᴇᴀᴅ ᴍᴏʀᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇɴᴜ ʙᴇʟᴏᴡ</i>"""
    HELP_TXT = """<b>𝙷𝙴𝚈 {}
 𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂.</b>"""
    PRIVATEBOT_TXT = """<b>Tʜᴀɴᴋs Fᴏʀ Aᴅᴅɪɴɢ Mᴇ</b>
 <b>›› Mᴜsᴛ Aᴅᴅ Mᴇ Aᴅᴍɪɴ Tᴏ Wᴏʀᴋ Oɴ Tʜɪs Gʀᴏᴜᴘ</b>

 <b>›› Cʜᴀɴɢᴇ Sᴇᴛᴛɪɴɢ Fᴏʀ Uʀ Gʀᴏᴜᴘ Cʟɪᴄᴋ 👉 /connect </b>

 <b>›› I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs/Sᴇʀɪᴇs Dᴏɴ'ᴛ Wᴏʀʀʏ</b>

 <b>›› Eɴᴊᴏʏ !! Mᴏʀᴇ Iɴғᴏ Usᴇ Uɴᴅᴇʀ Bᴜᴛᴛᴏɴs</b>"""   
    ABOUT_TXT = """🤖 ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/{}><b>AskAnyMovie</b></a>
 👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : AskAnyMovie
 📝 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏʀᴏɢʀᴀᴍ
 📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏᴛʜᴏɴ 3
 📡 ʜᴏsᴛᴇᴅ ᴏɴ : Render
 📢 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : <a href=https://t.me/askanymoviesupport></b><b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a><b>
 🌟 ᴠᴇʀsɪᴏɴ : ᴠ 4.0 [ ʙᴇᴛᴀ ]\n</b></i>"""
    SOURCE_TXT = """<b>NOTE:</b>
 - you will not get this source code as i t is built only to maintin Askanymovie. 
"""
    MANUAL_FILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of AskAnyMovie

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /enable_time - <code>to enable the reply for not available</code>
• /disable_time - <code>to disable the reply for not available</code>"""
    STATUS_TXT = """<b><u>Cᴜʀʀᴇɴᴛ Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛᴜs</b></u>
    
📑 ғɪʟᴇs sᴀᴠᴇᴅ: <code>{}</code>
👩🏻‍💻 ᴜsᴇʀs: <code>{}</code>
👥 ɢʀᴏᴜᴘs: <code>{}</code>
🗂️ ᴏᴄᴄᴜᴘɪᴇᴅ: <code>{}</code>
"""
    LOG_TXT_G = """#NewGroup
👥 ɢʀᴏᴜᴘ 👥 = {}(<code>{}</code>)
😇 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs 😇 = <code>{}</code>
💌 ᴀᴅᴅᴇᴅ ʙʏ 💌 - {} 
"""
    LOG_TXT_P = """#NewUser
ɪᴅ ♥️- <code>{}</code>
ɴᴀᴍᴇ 💥- {} 
"""
    POST_LINK_TXT = """Help: <b>post link</b>
<b>NOTE:</b>
1. The Link Of the Post is Copied and sent in with the title and audio 
2. used by only AskAnyMovie.
"""