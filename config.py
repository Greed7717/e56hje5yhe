from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

PROXY_URL = "http://proxy.server:3128"
storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN_ID = 879708821


BOT_PIC = '/Users/User/PycharmProjects/pythonProjectGeeks_33_1_bot/media/bot_pic.jpeg'
# ANIMATION_PIC = '/Users/bakyttynybekov/PycharmProjects/geek_33_1_bot/media/joinblink-blink.gif'
GROUP_ID = -1001965590722
DESTINATION_DIR = "/Users/User/PycharmProjects/pythonProjectGeeks_33_1_bot/media"