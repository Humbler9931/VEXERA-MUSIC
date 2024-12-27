import os
import aiohttp_session
from os import getenv
from dotenv import load_dotenv
from Abhixd.uptools import fetch_heroku_git_url

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQGcOCIAiYG0zbq7iIKoUCvarFjUwL7iU4IoitKLMwXTcHbXQMg6gkoyfEGszEeX5LzO6VyaAxjNkU7numNNVmUMel-Z0HllWPWMowMu2kFYMSNhL6T_nOHd4o7BPqHv9byZbZHXs8MHip-akQgfIZcF3-L2ln5vdCCaTuPbhXpqRjjy2EKrL_k2a3kZf50slrnupV_N0scjCLpzr35cOOG_GTqgVDJIQc9QbQnjT-raFuDeg51F-oHPtkuh7oHj-5cZtyUGoZvEnztcwA75-d3KMnCweprIBP4YR0JSCCTVRaLkT5r0jKge4OBISbZdfY-UMTKWg9CHHWbunZt9F7wljBs8iwAAAAGYTkO_AA")
BOT_TOKEN = getenv("7821128321:AAHUy0jo5JFoRTmYNNf5xBwLxrqxTQ_1oac")
BOT_NAME = getenv("BOT_NAME", "@II_RAJMUSIC_IIBOT")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/8628c642a266a22effd8c.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/4c39fbb88932761913fff.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/73e10ed6e2bd32b478de6.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
API_ID = int(getenv("27015202"))
API_HASH = getenv("b817ca2d21c5471522ec93b819301d56")
BOT_USERNAME = getenv("BOT_USERNAME", "@II_RAJMUSIC_IIBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "@II_PRIYA_RAJ_II")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "bestshayri_raj")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "mcqhi")
ARQ_API_KEY = getenv("ARQ_API_KEY", "WDOACF-QLNTOF-GBBGMZ-KOGZFW-ARQ")
# isi dengan username kamu tanpa simbol @
OWNER_NAME = getenv("OWNER_NAME", "promotionyoutubr")
# fill with your nickname
ALIVE_NAME = getenv("ALIVE_NAME", "promotionyoutubr")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("5789538424"))
DATABASE_URL = os.environ.get("mongodb+srv://nitishkypaurai17:RAJKUMARMOVIE@rajkumarmovie.qjhjk.mongodb.net/?retryWrites=true&w=majority&appName=RAJKUMARMOVIE")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("-1002293663374"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/levina-lab/VeezMusic"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
