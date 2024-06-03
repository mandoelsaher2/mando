import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from VeGaMusic import LOGGER, app, userbot
from VeGaMusic.core.call import Zoro
from VeGaMusic.misc import sudo
from VeGaMusic.plugins import ALL_MODULES
from VeGaMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


#──██████──────██████───█████████████──────██████████████───████████████████─────────
#──██──██──────██──██───██─────────██────██────────────██───██────────────██─────────
#──██──██──────██──██───██──█████████───██───████████████───██───███████──██─────────
#──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██─────────
#──██──██──────██──██───██──█▉──────────██──██──────────────██───██───██──██─────────
#──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██─────────
#──██──██──────██──█▉───██──██──────────██──██──────────────██───██───██──██─────────
#──██──██──────██──██───██──█████████───██──█▉───███████────██───███████──██─────────
#──██───██────██───██───██─────────██───██──██───██────██───██────────────██─────────
#───██───██──██───██────██──█████████───██──██───████──██───██───███████──██─────────
#────██───████───██─────██──██──────────██──██─────██──██───██───██───██──██─────────
#─────██───██───██──────██──██──────────██───██────██──██───██───██───██──██─────────
#──────██──────██───────██──██───────────██───██───██──██───██───██───██──██─────────
#───────██────██────────██──█████████─────██──███████──██───██───██───██──██─────────
#────────██──██─────────██─────────█▉──────██──────────██───██───██───██──██─────────
#─────────████──────────█████████████───────████████████────███████───██████─────────

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("كود جلسة الحساب المساعد غير مدعوم ...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VeGaMusic.plugins" + all_module)
    LOGGER("ميوزك الساحر").info("تم تحميل الاضافات ...✓")
    await userbot.start()
    await Zoro.start()

    await Zoro.decorators()
    LOGGER("ميوزك الساحر").info("──██████──────██████───█████████████──────██████████████───████████████████─────────\n──██──██──────██──██───██─────────██────██────────────██───██────────────██─────────\n──██──██──────██──██───██──█████████───██───████████████───██───███████──██─────────\n──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██─────────\n──██──██──────██──██───██──█▉──────────██──██──────────────██───██───██──██─────────\n──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██─────────\n──██──██──────██──█▉───██──██──────────██──██──────────────██───██───██──██─────────\n──██──██──────██──██───██──█████████───██──█▉───███████────██───███████──██─────────\n──██───██────██───██───██─────────██───██──██───██────██───██────────────██─────────\n───██───██──██───██────██──█████████───██──██───████──██───██───███████──██─────────\n────██───████───██─────██──██──────────██──██─────██──██───██───██───██──██─────────\n─────██───██───██──────██──██──────────██───██────██──██───██───██───██──██─────────\n──────██──────██───────██──██───────────██───██───██──██───██───██───██──██─────────\n───────██────██────────██──█████████─────██──███████──██───██───██───██──██─────────\n────────██──██─────────██─────────█▉──────██──────────██───██───██───██──██─────────\n─────────████──────────█████████████───────████████████────███████───██████─────────")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ميوزك الساحر").info("جارِ ايقاف بوت الميوزك . . .")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
