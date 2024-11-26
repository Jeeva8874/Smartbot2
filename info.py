import re
import os
from os import environ,getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
#---------------------------------------------------------------
#---------------------------------------------------------------         ,
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '22977776'))
API_HASH = environ.get('API_HASH', '2ac7223d720bdeec757cbc88ced57224')
BOT_TOKEN = environ.get('BOT_TOKEN', '6700618694:AAHDAmKEbokn-5GkpseIVWGIyZTM2YZs2WQ')
#---------------------------------------------------------------
#---------------------------------------------------------------
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6762558871').split()]
USERNAME = environ.get('USERNAME', "https://t.me/Heart_thieft") # ADMIN USERNAME
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002391269521'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/Movieprovidergroups')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002480489590').split()]
#---------------------------------------------------------------
#---------------------------------------------------------------
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Ajifilterbot:1055221@heartfilter.pjrma.mongodb.net/?retryWrites=true&w=majority&appName=HeartFilter")
DATABASE_NAME = environ.get('DATABASE_NAME', "heartfilter")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
#---------------------------------------------------------------
#---------------------------------------------------------------
#----------- There will be channel id add in all these ---------
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002479542941'))  # set shortner log channel
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1002494713645')) # The movie you upload in it will be deleted from the bot.
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002393358982'))
auth_channel = environ.get('AUTH_CHANNEL', '-1002181741528')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002329218829'))
request_channel = environ.get('REQUEST_CHANNEL', '-1002369002372') # If anyone sends a request message to your bot, you will get it in this channel.
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002387499459')) # 
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/cc_support_group') #Support group link ( make sure bot is admin )
#---------------------------------------------------------------
#---------------------------------------------------------------
IS_VERIFY = is_enabled('IS_VERIFY', True)
#---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://t.me/How_To_Get_Movie")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/How_To_Get_Movie")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/How_To_Get_Movie")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "69bfe45fc35b6b3178b4b95de9ef1db14a746ce7")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'modijiurl.com')
SHORTENER_API2 = environ.get("SHORTENER_API2", "69bfe45fc35b6b3178b4b95de9ef1db14a746ce7")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'modijiurl.com')
SHORTENER_API3 = environ.get("SHORTENER_API3", "69bfe45fc35b6b3178b4b95de9ef1db14a746ce7")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'modijiurl.com')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))
#---------------------------------------------------------------
#---------------------------------------------------------------
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
#---------------------------------------------------------------
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
START_IMG = (environ.get('START_IMG', 'https://envs.sh/Sau.jpg https://envs.sh/Sat.jpg https://envs.sh/Sai.jpg https://envs.sh/Sab.jpg https://envs.sh/Saq.jpg https://envs.sh/SaS.jpg https://envs.sh/SaW.jpg https://envs.sh/SaB.jpg https://envs.sh/SaI.jpg https://envs.sh/San.jpg https://envs.sh/SaT.jpg https://envs.sh/Sap.jpg')).split()
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg')
REFER_PICS = (environ.get("REFER_PICS", "https://envs.sh/PSI.jpg")).split() 
PAYPICS = (environ.get('PAYPICS', 'https://i.ibb.co/LY0LbqQ/image.jpg')).split()
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/55a5392f88ec5a4bd3379.jpg'))
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
IS_SEND_MOVIE_UPDATE = is_enabled('IS_SEND_MOVIE_UPDATE', False) # Don't Change It ( If You Want To Turn It On Then Turn It On By Commands) We Suggest You To Make It Turn Off If You Are Indexing Files First Time.
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', True)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase
# Online Stream and Download

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "https://premiumbot.koyeb.app/")

#---------------------------------------------------------------
#---------------------------------------------------------------
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'tutorial_2': TUTORIAL_2,
            'tutorial_3': TUTORIAL_3,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
}

#Newfeatures vars developer - Anshvachhani99 ✨🌸
DIRECT_GEN_DB = int(os.environ.get("DIRECT_GEN_DB", "-1002391269521"))
DIRECT_GEN_URL = os.environ.get("DIRECT_GEN_URL", "https://premiumbot.koyeb.app/")
DIRECT_GEN = bool(DIRECT_GEN_DB and DIRECT_GEN_URL)

POST_MODE= bool(environ.get('POST_MODE', True))
POST_SHORT_API = environ.get('POST_SHORT_API', '')
POST_SHORT_URL = environ.get('POST_SHORT_URL', '')

HOW_TO_POST_SHORT = environ.get('HOW_TO_POST_SHORT', 'https://t.me/Howtodowloa/9')
