import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = """<b>💤𝖶𝖾𝗅𝖼𝗈𝗆𝖾💤\n {} 🍎 ɪᴍ 『 ғɪʟᴛᴇʀ ʙᴏᴛ 』 𝖨 𝖢𝖺𝗇 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝖬𝗈𝗏𝗂𝖾𝗌/𝖳𝗏 𝖲𝖾𝗋𝗂𝖾𝗌 \n 🍒𝖬𝖺𝗂𝗇𝗍𝖺𝗂𝗇 <a href=https://t.me/vimukthioshada></b><b>𝗩𝗶𝗺𝘂𝗸𝘁𝗵𝗶 𝗢𝘀𝗵𝗮𝗱𝗮 :)</a><b></b>
    
<i>𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 😌\n𝖱𝖾𝖺𝖽 𝖬𝖾𝗇𝗎</i>"""
    HELP_TXT = """<b>𝖶𝖾𝗅𝖼𝗈𝗆𝖾 {}
𝖧𝖾𝗋𝖾 𝖨𝗌 𝖬𝗒 𝖢𝗈𝗆𝗆𝖺𝗇𝖽.</b>"""
    PRIVATEBOT_TXT = """<b>𝖳𝗁𝖺𝗇𝗄 𝖥𝗈𝗋 𝖠𝖽𝖽 𝖬𝖾 🍎</b>
<b>›› 𝖯𝗅𝗓 𝖠𝖽𝖽 𝖬𝖾 𝖠𝖽𝗆𝗂𝗇 𝖳𝗈 𝖶𝗈𝗋𝗄 𝖮𝗇 𝖳𝗁𝗂𝗌 𝖦𝗋𝗈𝗎𝗉</b>

<b>›› Cʜᴀɴɢᴇ Sᴇᴛᴛɪɴɢ Fᴏʀ Uʀ Gʀᴏᴜᴘ Cʟɪᴄᴋ 👉 /connect </b>

<b>›› I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs/Sᴇʀɪᴇs Dᴏɴ'ᴛ Wᴏʀʀʏ</b>

<b>›› Eɴᴊᴏʏ !! Mᴏʀᴇ Iɴғᴏ Usᴇ Uɴᴅᴇʀ Bᴜᴛᴛᴏɴs</b>"""
    
    ABOUT_TXT = """🤖𝖬𝗒 𝖭𝖺𝗆𝖾 : <a href=https://t.me/{}><b>𝖥𝗂𝗅𝗆𝗌𝖲𝗍𝗎𝖽𝗂𝗈 𝖬𝗈𝗏𝗂𝖾𝗌/𝖡𝗈𝗍</b></a>
👨‍💻 𝖮𝗐𝗇𝖾𝗋 : <a href=https://t.me/vimukthioshada></b><b>𝖵𝗂𝗆𝗎𝗄𝗍𝗁𝗂<b></a>
📝 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏʀᴏɢʀᴀᴍ
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏᴛʜᴏɴ 3
📡 ʜᴏsᴛᴇᴅ ᴏɴ : 𝖭𝖺𝗌𝖺 🌎
📢 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : <a href=https://t.me/Filmstudiodl></b><b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a><b>
🌟 ᴠᴇʀsɪᴏɴ : ᴠ 4.0 [ ʙᴇᴛᴀ ]\n</b></i>"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  
<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

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
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
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
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
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
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b><u>Cᴜʀʀᴇɴᴛ Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛᴜs</b></u>
    
📑 ғɪʟᴇs sᴀᴠᴇᴅ: <code>{}</code>
👩🏻‍💻 ᴜsᴇʀs: <code>{}</code>
👥 ɢʀᴏᴜᴘs: <code>{}</code>
🗂️ ᴏᴄᴄᴜᴘɪᴇᴅ: <code>{}</code>
"""
    LOG_TEXT_G = """#NewGroup
👥 ɢʀᴏᴜᴘ 👥 = {}(<code>{}</code>)
😇 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs 😇 = <code>{}</code>
💌 ᴀᴅᴅᴇᴅ ʙʏ 💌 - {} 
"""
    LOG_TEXT_P = """#NewUser
ɪᴅ ♥️- <code>{}</code>
ɴᴀᴍᴇ 💥- {} 
"""
