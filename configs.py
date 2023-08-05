import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", "22501624"))
    API_HASH = os.getenv("API_HASH", "5181e32c508753a0fdf347d6d3a0478c")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5986737297:AAGu5jcyi0V0cPOfEQ6R_kRhwN8divRSiuQ")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MaxxBot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "1BVtsOIgBuzBnxJc1Xca2dvdpMU8kndwXss7iBnffuhwA_YPpanLjvpwTaxeQI_QNNtUcs7XH66hL2miRdGw4hzk-1q71ZyIf1cWVWpCIe_Yb9BaQMs2eMp4s5AewjTDr66vkseKSQBriEH2my0fY_1Ff_IDLVaRR8JmtEU5VuYlalrmYRDwdwD3LR0utaHbwCvQvtOWb-xS2JhH7N-a3d5d29T-O8KhEsgCM0LySZVcbJSgi4Eq49x3dEyj0FisHI51Kqt0SaCzWbpK-XtxTXc46i6m7nb9TuBIU7h-M3zGBjv2UnJGdj75nvqHmXcFxDPW2QWhiqzsPt2XALNsschqNoURs92Q=")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001899641345")) 
    BOT_USERNAME = os.getenv("BOT_USERNAME", "Maxxmoviesrobot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "1913687836"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Royaldwip")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "DOON_MoVies")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", """<b>Hᴇʏ, {}! 😃\n\nI Aᴍ A Sɪᴍᴘʟᴇ Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ Bᴏᴛ. 😅\n\nYᴏᴜ Cᴀɴ Aᴅᴅ Mᴇ Oɴ Yᴏᴜʀ Gʀᴏᴜᴘ As Aᴅᴍɪɴ 🤪\n\nNᴏᴛᴇ - ɪ ᴄᴀɴ Pʀᴏᴠɪᴅᴇ Yᴏᴜʀ Mᴏᴠɪᴇs Lɪɴᴋs Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ 😜\n\nFᴏʀ ᴍᴏʀᴇ ɪɴғᴏ Cʟɪᴄᴋ Oɴ /help ✅</b>""" ) 
    START_PHOTO = os.getenv("START_PHOTO", "https://graph.org/file/35c29ce1137d0e07e557d.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", """<b>Hᴇʏ, {}! 😃\n\nI Aᴍ A Sɪᴍᴘʟᴇ Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ Bᴏᴛ. 😅\n\nYᴏᴜ Cᴀɴ Aᴅᴅ Mᴇ Oɴ Yᴏᴜʀ Gʀᴏᴜᴘ As Aᴅᴍɪɴ 🤪\n\nNᴏᴛᴇ - ɪ ᴄᴀɴ Pʀᴏᴠɪᴅᴇ Yᴏᴜʀ Mᴏᴠɪᴇs Lɪɴᴋs Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ 😜\n\nFᴏʀ ᴍᴏʀᴇ ɪɴғᴏ Cʟɪᴄᴋ Oɴ /help ✅</b>""" )
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1001753192788")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Maxxbot:Maxxbot@cluster0.gv1e7ee.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", '-1001817141728')
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "DOON_MoVies")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 180))
    MDISK_API = os.getenv("MDISK_API", "Qu7jX9V0Sn3q1JHdxjPp")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", """@RoyalDwip""")
    ABOUT_WATCH_TEXT = """@RoyalDwip"""
    
    ABOUT_TERABOX_TEXT = """
𝗧𝗲𝗿𝗮𝗕𝗼𝘅 𝗸𝗶 𝗹𝗶𝗻𝗸𝘀 𝗢𝗽𝗲𝗻 𝗔𝗶𝘀𝗲 𝗞𝗮𝗿𝗲👇🔥
वीडियो प्ले करने में कोई प्रोब्लम अ रही हो तो इक बार रजिस्ट्रेशन कर ले फिर आप बिना एड के विडियो अच्छे से चला पाएंगे थैंक्यू 😊👍

https://teraboxapp.com/s/1IlxmTsmTLQ-dM1AmaHJmZQ

1) 𝘛𝘦𝘳𝘢𝘣𝘰𝘹 𝘬𝘪 𝘭𝘪𝘯𝘬 𝘱𝘦𝘳 𝘤𝘭𝘪𝘤𝘬 𝘬𝘢𝘳𝘦 𝘶𝘴𝘬𝘦 𝘣𝘢𝘢𝘥 𝘢𝘪𝘴𝘢 𝘱𝘢𝘨𝘦 𝘬𝘩𝘶𝘭𝘦𝘨𝘢.

2) 𝘜𝘱𝘱𝘢𝘳 𝘴𝘪𝘥𝘦 𝘭𝘰𝘨𝘪𝘯/𝘙𝘦𝘨𝘪𝘴𝘵𝘳𝘢𝘵𝘪𝘰𝘯 𝘭𝘪𝘬𝘩𝘢 𝘩𝘰𝘨𝘢 𝘶𝘴𝘱𝘦 𝘤𝘭𝘪𝘤𝘬 𝘬𝘢𝘳𝘰.😉

3) 𝘗𝘩𝘪𝘳 𝘳𝘦𝘨𝘪𝘴𝘵𝘳𝘢𝘵𝘪𝘰𝘯 𝘬𝘢𝘳𝘰 𝘢𝘶𝘳 𝘭𝘪𝘧𝘦 𝘵𝘪𝘮𝘦 𝘧𝘳𝘦𝘦 𝘷𝘪𝘥𝘦𝘰𝘴 𝘣𝘪𝘯𝘢 𝘈𝘥𝘴 𝘬𝘦 𝘥𝘦𝘬𝘩𝘰😍

4) 𝘕𝘢𝘩𝘪 𝘛𝘰 𝘈𝘱𝘱 𝘕𝘪𝘤𝘩𝘦 𝘋𝘪𝘺𝘦 𝘎𝘢𝘺𝘦  𝘗𝘢𝘳 𝘊𝘭𝘪𝘤𝘬 𝘒𝘢𝘳𝘬𝘦 𝘗𝘶𝘳𝘢 𝘚𝘵𝘦𝘱 𝘓𝘪𝘷𝘦 𝘗𝘩𝘰𝘵𝘰 𝘔𝘦 𝘋𝘦𝘬𝘩 𝘚𝘬𝘢𝘵𝘦 𝘏𝘢𝘪😇"""

    ABOUT_HELP_TEXT = """<b>🍓 RᴇQᴜɪʀᴇᴍᴇɴᴛ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ!

🍓 Sᴛᴇᴘ 1 - Aᴘᴋᴏ ᴇᴋ ɢʀᴏᴜᴘ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴍᴇᴍʙᴇʀꜱ ʙʜɪ ʜᴏ, ᴀᴜʀ ᴇᴋ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴀᴘᴋᴇ ꜱᴀʀᴇ ᴘᴏꜱᴛ ʜᴏɴɢᴇ!

🍓 Sᴛᴇᴘ 2 - ʙᴏᴛ ᴋᴏ ᴀᴘɴᴇ ɢʀᴏᴜᴘ ᴀᴜʀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋᴀ ᴀᴅᴍɪɴ ʙᴀɴᴀɴᴀ ʜᴏɢᴀ.

🍓 Sᴛᴇᴘ 3 - ɢʀᴏᴜᴘ ᴍᴇ "/License" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ!

ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ. @Dreamer999

🍓 Sᴛᴇᴘ 4 - ɢʀᴏᴜᴘ ᴍᴇ "/database - ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ɪᴅ" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ.

ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ʙʜɪ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ. @Dreamer999

🍓 Sᴛᴇᴘ 5 - ᴀʙ ᴀᴘᴋᴏ ᴀᴘɴᴇ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴘᴏꜱᴛ ᴅᴀʟɴɪ ʜᴏɢɪ,

ᴊɪꜱꜱᴇ ᴋɪ ᴀɢᴀʀ ɢʀᴏᴜᴘ ᴍᴇ ᴋᴏɪ ᴜꜱᴇʀ ꜱᴇᴀʀᴄʜ ᴋᴀʀᴇ ᴛᴏ ʏᴇ ʙᴏᴛ ᴜɴ ᴜꜱᴇʀ ᴋᴇ Qᴜᴀʀʏ ᴋᴏ ꜱᴀᴍᴀᴊʜ ᴋᴇ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ꜱᴇ ᴘᴏꜱᴛ ᴜᴛʜᴀ ᴋᴇ ᴜɴʜᴇ ᴅᴇ ᴘᴀʏᴇ.

🍓 Nᴏᴛᴇ : Bᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴊᴏɪɴ ʜᴏɴᴇ ᴄʜᴀʜɪʏᴇ,

ᴀɢᴀʀ ʙᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴀ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ɴʜɪ ᴋᴀʀ ʀᴀʜᴇ ʜᴀɪɴ ᴛᴏ ᴜɴʜᴇ ᴘᴇʀꜱᴏɴᴀʟ ᴍꜱɢ ᴋᴀʀᴇɴ.
👉 @Dreamer999

☘️ Tip : Contact @Dreamer999 For Rent Me !</b>"""

