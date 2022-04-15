import asyncio
import random
import glob
import re
import shutil
import urllib
import base64
import requests
import time
import shlex
import math
import os
import html
import io
import sys
import traceback
import cv2
from asyncio import sleep
import telethon.password as pwd_mod
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.events import CallbackQuery
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.errors import FloodWaitError
from telethon.tl import functions
from urlextract import URLExtract
from requests import get
from typing import Optional, Tuple
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events
from telethon.utils import pack_bot_file_id, get_input_location
from telethon.tl.custom import Dialog
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import Channel, Chat, User
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from asyncio.exceptions import TimeoutError as AsyncTimeout
from telethon.errors.rpcerrorlist import MessageTooLongError, YouBlockedUserError
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantsBots
from telethon.tl.types import DocumentAttributeVideo as video
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.types import InputMessagesFilterMusic
from telethon.tl.functions.messages import SaveDraftRequest
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from ..helpers.progress import humanbytes as hb
from userbot.utils import admin_cmd, sudo_cmd, eor
from telethon.utils import get_display_name
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from ..helpers.utils import reply_id as rd
from telethon.tl.types import Channel, Chat, InputPhoto, User
from userbot import iqthon
from userbot.core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, AUTONAME, BOTLOG, BOTLOG_CHATID, DEFAULT_BIO, get_user_from_event
from ..helpers import get_user_from_event, reply_id
from ..sql_helper.locks_sql import *
from ..helpers.functions import deEmojify, hide_inlinebot, waifutxt
from userbot.utils.decorators import register
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format
from userbot.helpers.functions import convert_toimage,    deEmojify,    phcomment,    threats,    trap,    trash
from userbot.helpers.functions import convert_tosticker,    flip_image,    grayscale,    invert_colors,    mirror_file,    solarize
from ..sql_helper.global_list import add_to_list, get_collection_list, is_in_list, rm_from_list
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.locks_sql import *

from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps
from . import AUTONAME, BOTLOG, BOTLOG_CHATID, DEFAULT_BIO, _catutils, edit_delete, iqthon, logging, spamwatch    

@iqthon.on(admin_cmd(pattern="(الايدي|id)(?: |$)(.*)"))
async def _(event):
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{str(e)}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(                    event, f"**🇮🇶 ⦙   آيـدي المُستخدم 💠 :** `{input_str}` هـو `{p.id}`"                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(                        event, f"**🇮🇶 ⦙   آيـدي الدردشــــة 💠 :** `{p.title}` هـو `{p.id}` "                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "**🇮🇶 ⦙   قُم بإدخال أسم مُستخدم أو الرد على المُستخدم 🇮🇶**")
    elif event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(                event,                f"**🇮🇶 ⦙   آيـدي الدردشــــة   : **`{str(event.chat_id)}` \n**🇮🇶 ⦙   آيـدي المُستخدم   : **`{str(r_msg.sender_id)}` \n**🇮🇶 ⦙  آيـدي الميديـا   : **`{bot_api_file_id}`"            )
        else:
            await edit_or_reply(                event,                f"**🇮🇶 ⦙   آيـدي الدردشــــة   : **`{str(event.chat_id)}` \n**🇮🇶 ⦙   آيـدي المُستخدم   : **`{str(r_msg.sender_id)}` "            )
@iqthon.on(admin_cmd(pattern=f"{plagiarism}(?: |$)(.*)"))
async def _(event):
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return
    user_id = replied_user.id
    profile_pic = await event.client.download_profile_photo(user_id, Config.TEMP_DIR)
    first_name = html.escape(replied_user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = replied_user.about
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))
    pfile = await event.client.upload_file(profile_pic)
    await event.client(functions.photos.UploadProfilePhotoRequest(pfile))
    await edit_delete(event, "**🇮🇶 ⦙   تـم إنتحـال الحسـاب بنجـاح  ✓**")
    if BOTLOG:
        await event.client.send_message(            BOTLOG_CHATID,            f"**🇮🇶 ⦙  الإنتحـال 🃏 :** \n **✓ تـم إنتحـال الحسـاب بنجـاح :**  [{first_name}](tg://user?id={user_id })"        )
async def autobio_loop():
    AUTOBIOSTART = gvarstatus(f"{OR_AUTOBIO}") == "true"
    while AUTOBIOSTART:
        HM = time.strftime("%I:%M")
        Dont1Tags = gvarstatus("FONTS_AUTO") or "font1"
        FONT1 = requests.get(f"https://klanrsulten.ml/FONTS/{Dont1Tags}.php?text={HM}").json()['newText']
        bio = f"{EMOJI_TELETHON} {DEFAULTUSERBIO}  - {FONT1}"
        LOGS.info(bio)
        try:
            await iqthon(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTOBIOSTART = gvarstatus(f"{OR_AUTOBIO}") == "true"
@iqthon.on(admin_cmd(pattern=f"{unplagiarism}(?: |$)(.*)"))
async def _(event):
    name = f"{DEFAULTUSER}"
    blank = ""
    bio = f"{DEFAULTUSERBIO}"
    await event.client(
        functions.photos.DeletePhotosRequest(            await event.client.get_profile_photos("me", limit=1)        )    )
    await event.client(functions.account.UpdateProfileRequest(about=bio))
    await event.client(functions.account.UpdateProfileRequest(first_name=name))
    await event.client(functions.account.UpdateProfileRequest(last_name=blank))
    await edit_delete(event, "**🇮🇶 ⦙  تمّـت إعـادة حسـابك بنجـاح **")
    if BOTLOG:
        await event.client.send_message(            BOTLOG_CHATID, f"🇮🇶 ⦙   **الأعـادة  :**\n**🇮🇶 ⦙   تـم إعـادة ضبـط حسـابك إلـى وضعـه الطبيـعي بـنجاح **"        )

async def fetch_info(replied_user, event):
    replied_user_profile_photos = await event.client(        GetUserPhotosRequest(            user_id=replied_user.user.id, offset=42, max_id=0, limit=80        )    )
    replied_user_profile_photos_count = "`لم يقم المستخدم بتعيين صورة الملف الشخصي`"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception:
        dc_id = "`تعذر جلب معرف DC`"
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = replied_user.user.bot
    restricted = replied_user.user.restricted
    verified = replied_user.user.verified
    photo = await event.client.download_profile_photo(        user_id,        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",        download_big=True    )
    first_name = (        first_name.replace("\u2060", "")        if first_name        else ("`هذا المستخدم ليس له اسم`")    )
    last_name = last_name.replace("\u2060", "") if last_name else (" ")
    username = "@{}".format(username) if username else ("`ᴛʜɪs ᴘᴇʀsᴏɴ ᴅᴏᴇs ɴᴏᴛ ʜᴀᴠᴇ ᴀɴ ᴜsᴇʀ`")
    user_bio = "`ᴛʜɪs ᴘᴇʀsᴏɴ ʜᴀs ɴᴏ ᴘʀᴏғɪʟᴇ`" if not user_bio else user_bio
    caption = "<b>𓍹ⵧⵧⵧⵧⵧⵧⵧⵧ⁦⁦ⵧⵧⵧⵧⵧⵧⵧⵧ𓍻</b>\n"
    caption += f"<b>• 🇮🇶 | 𝗡𝗔𝗠𝗘  :  </b> {first_name} {last_name}\n"
    caption += f"<b>• 🇮🇶 | 𝗨𝗦𝗘𝗥  : </b> {username}\n"
    caption += f"<b>• 🇮🇶 | 𝗜𝗗  :  </b> <code>{user_id}</code>\n"
    caption += f"<b>• 🇮🇶 | 𝗡𝗨𝗠𝗕𝗘𝗥 𝗣𝗛𝗢𝗧𝗢𝗦  : </b> {replied_user_profile_photos_count}\n"
    caption += f"<b>• 🇮🇶 | 𝗔𝗖𝗖𝗢𝗨𝗡𝗧  :  </b> "
    caption += f' <a href="tg://user?id={user_id}">{first_name}{last_name}</a> \n'
    caption += "<b>𓍹ⵧⵧⵧⵧⵧⵧⵧⵧ⁦⁦ⵧⵧⵧⵧⵧⵧⵧⵧ𓍻</b>\n"
    return photo, caption
async def autoname_loop():
    AUTONAMESTART = gvarstatus(f"{OR_NAMEAUTO}") == "true"
    while AUTONAMESTART:
        HM = time.strftime("%I:%M")
        Dont1Tags = gvarstatus(f"FONTS_AUTO") or "font1"
        FONT1 = requests.get(f"https://klanrsulten.ml/FONTS/{Dont1Tags}.php?text={HM}").json()['newText']
        name = f"{EMOJI_TELETHON} {FONT1} | "
        LOGS.info(name)
        try:
            await iqthon(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTONAMESTART = gvarstatus(f"{OR_NAMEAUTO}") == "true"
@iqthon.on(admin_cmd(pattern="كشف(?:\s|$)([\s\S]*)"))
async def _(event):
    replied_user, error_i_a = await get_user_from_event(event)
    if not replied_user:
        return
    catevent = await edit_or_reply(event, "جاري الكشف عن الشخص")
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    user_id = replied_user.user.id
    first_name = html.escape(replied_user.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    common_chats = replied_user.common_chats_count
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception:
        dc_id = " عذرا لانقدر على جلب المعلومات الخاصه له!"
    if spamwatch:
        ban = spamwatch.get_ban(user_id)
        if ban:
            sw = f"**حظر المشاهد :** `شغال` \n       **-**🤷‍♂️**السبب : **`{ban.reason}`"
        else:
            sw = f"**حظر المشاهد :** `معطل`"
    else:
        sw = "**محظور المشاهد :**`غير متصل`"
    try:
        casurl = "https://api.cas.chat/check?user_id={}".format(user_id)
        data = get(casurl).json()
    except Exception as e:
        LOGS.info(e)
        data = None
    if data:
        if data["ok"]:
            cas = "**الحظر :** `محظور`"
        else:
            cas = "**الحظر :** `لست محضور`"
    else:
        cas = "**الحظر :** `لايمكن جلب معلومات الشخص`"
    caption = """**معلومات حول : [{}](tg://user?id={}):
   -🔖 الايدي : **`{}`
   **-**👥**المجموعات المشتركة : **`{}`
   **-**🌏**رقم مركز البيانات : **`{}`
   **-**🔏**مقيد من تليجرام : **`{}`
   **-**🦅{}
   **-**👮‍♂️{}
""".format(        first_name,
        user_id,
        user_id,
        common_chats,
        dc_id,
        replied_user.user.restricted,
        sw,
        cas    )
    await edit_or_reply(catevent, caption)
@iqthon.on(admin_cmd(pattern=f"{idee}(?:\s|$)([\s\S]*)"))
async def who(event):
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user, reason = await get_user_from_event(event)
    if not replied_user:
        return
    cat = await edit_or_reply(event, "**• 🇮🇶 | جـاري جـلب ايـدي المسـتخدم  **")
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await edit_or_reply(cat, "**• 🇮🇶 | تعذر جلب معلومات هذا المستخدم.**")
    message_id_to_reply = await reply_id(event)
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html"        )
        if not photo.startswith("http"):
            os.remove(photo)
        await cat.delete()
    except TypeError:
        await cat.edit(caption, parse_mode="html")
FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
TELEGRAPH_MEDIA_LINKS = [    "https://telegra.ph/file/e354ce72d5cc6a1d27c4d.jpg",    "https://telegra.ph/file/8f9ff3d743e6707a61489.jpg",    "https://telegra.ph/file/bfc97f4abc4bec6fe860d.jpg",    "https://telegra.ph/file/5ef0f060023600ec08c19.jpg",    "https://telegra.ph/file/a448465a3a8a251170f76.jpg",    "https://telegra.ph/file/eb0ac1557668a98a38cb6.jpg",    "https://telegra.ph/file/fdb3691a17a2c91fbe76c.jpg",    "https://telegra.ph/file/ccdf69ebf6cb85c52a25b.jpg",    "https://telegra.ph/file/2adffc55ac0c9733ecc7f.jpg",    "https://telegra.ph/file/faca3b435da33f2f156f1.jpg",    "https://telegra.ph/file/93d0a48c31e16f036f0e8.jpg",    "https://telegra.ph/file/9ed89dc742b172a779312.jpg",    "https://telegra.ph/file/0b4c19a19fb834d922d66.jpg",    "https://telegra.ph/file/a95a0deb86f642129b067.jpg",    "https://telegra.ph/file/c4c3d8b5cfc3cc5040833.jpg",    "https://telegra.ph/file/1e1a1b52b9a313e066a04.jpg",    "https://telegra.ph/file/a582950a8a259efdcbbc0.jpg",    "https://telegra.ph/file/9c3a784d45790b193ca36.jpg",    "https://telegra.ph/file/6aa74b17ae4e7dc46116f.jpg",    "https://telegra.ph/file/e63cf624d1b68a5c819b6.jpg",    "https://telegra.ph/file/7e420ad5995952ba1c262.jpg",    "https://telegra.ph/file/c7a4dc3d2a9a422c19723.jpg",    "https://telegra.ph/file/163c7eba56fd2e8c266e4.jpg",    "https://telegra.ph/file/5c87b63ae326b5c3cd713.jpg",    "https://telegra.ph/file/344ca22b35868c0a7661d.jpg",    "https://telegra.ph/file/a0ef3e56f558f04a876aa.jpg",    "https://telegra.ph/file/217b997ad9b5af8b269d0.jpg",    "https://telegra.ph/file/b3595f99b221c56a5679b.jpg",    "https://telegra.ph/file/aba7f4b4485c5aae53c52.jpg",    "https://telegra.ph/file/209ca51dba6c0f1fba85f.jpg",    "https://telegra.ph/file/2a0505ee2630bd6d7acca.jpg",    "https://telegra.ph/file/d193d4191012f4aafd4d2.jpg",    "https://telegra.ph/file/47e2d151984bd54a5d947.jpg",    "https://telegra.ph/file/2a6c735b47db947b44599.jpg",    "https://telegra.ph/file/7567774412fb76ceba95c.jpg",    "https://telegra.ph/file/6dd8b0edec92b24985e13.jpg",    "https://telegra.ph/file/dcf5e16cc344f1c030469.jpg",    "https://telegra.ph/file/0718be0bd52a2eb7e36aa.jpg",    "https://telegra.ph/file/0d7fcb82603b5db683890.jpg",    "https://telegra.ph/file/44595caa95717f4db4788.jpg",    "https://telegra.ph/file/f3a063d884d0dcde437e3.jpg",    "https://telegra.ph/file/733425275da19cbed0822.jpg",    "https://telegra.ph/file/aff5223e1aa29f212a46a.jpg",    "https://telegra.ph/file/45ccfa3ef878bea9cfc02.jpg",    "https://telegra.ph/file/a38aa50d009835177ac16.jpg",    "https://telegra.ph/file/53e25b1b06f411ec051f0.jpg",    "https://telegra.ph/file/96e801400487d0a120715.jpg",    "https://telegra.ph/file/6ae8e799f2acc837e27eb.jpg",    "https://telegra.ph/file/265ff1cebbb7042bfb5a7.jpg",    "https://telegra.ph/file/4c8c9cd0751eab99600c9.jpg",    "https://telegra.ph/file/1c6a5cd6d82f92c646c0f.jpg",    "https://telegra.ph/file/2c1056c91c8f37fea838a.jpg",    "https://telegra.ph/file/f140c121d03dfcaf4e951.jpg",    "https://telegra.ph/file/39f7b5d1d7a3487f6ba69.jpg",]
@iqthon.on(admin_cmd(pattern="رابطه(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"⨳ | [{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"⨳ | [{tag}](tg://user?id={user.id})")
@iqthon.on(admin_cmd(pattern="اسمه(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"⨳ | {custom} ")
    ll5 = user.first_name.replace("\u2060", "") if user.first_name else (" ")
    kno = user.last_name.replace("\u2060", "") if user.last_name else (" ")
    await edit_or_reply(mention, f"⨳  {ll5} {kno}")  
@iqthon.on(admin_cmd(pattern="صورته(?:\s|$)([\s\S]*)"))
async def potocmd(event):
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if uid.strip() == "":
        uid = 1
        if int(uid) > (len(photos)):
            return await edit_delete(                event, "**🇮🇶 ⦙   لم يتم العثور على صورة لهذا  الشخص **"            )
        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    elif uid.strip() == "جميعها":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if u:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except Exception:
                return await edit_delete(event, "**🇮🇶 ⦙   هذا المستخدم ليس لديه صور لتظهر لك    **")
    else:
        try:
            uid = int(uid)
            if uid <= 0:
                await edit_or_reply(                    event, "**🇮🇶 ⦙   الرقم غير صحيح - اختر رقم صوره موجود فعليا **"                )
                return
        except BaseException:
            await edit_or_reply(event, "**🇮🇶 ⦙   هناك خطا  ⁉️**")
            return
        if int(uid) > (len(photos)):
            return await edit_delere(                event, "**🇮🇶 ⦙   لم يتم العثور على صورة لهذا  الشخص **"            )

        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    await event.delete()  
    @iqthon.on(admin_cmd(pattern="وضع معرف(?: |$)(.*)"))
async def update_username(username):
    newusername = username.pattern_match.group(1)
    try:
        await username.client(UpdateUsernameRequest(newusername))
        await edit_delete(event, USERNAME_SUCCESS)
    except UsernameOccupiedError:
        await edit_or_reply(event, USERNAME_TAKEN)
    except Exception as e:
        await edit_or_reply(event, f"**🇮🇶 ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
@iqthon.on(admin_cmd(pattern=r"شوت ?(.*)", outgoing=True))
async def shout(args):
    if args.fwd_from:
        return
    else:
        msg = "```"
        messagestr = args.text
        messagestr = messagestr[7:]
        text = " ".join(messagestr)
        result = []
        result.append(" ".join([s for s in text]))
        for pos, symbol in enumerate(text[1:]):
            result.append(symbol + " " + "  " * pos + symbol)
        result = list("\n".join(result))
        result[0] = text[0]
        result = "".join(result)
        msg = "\n" + result
        await eor(args, "`" + msg + "`")

if 1 == 1:
    name = "Profile Photos"
    client = borg

    @iqthon.on(admin_cmd(pattern="الصور ?(.*)"))
    async def potocmd(event):
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
        else:
            photos = await event.client.get_profile_photos(chat)
        if id.strip() == "":
            try:
                await event.client.send_file(event.chat_id, photos)
            except a:
                photo = await event.client.download_profile_photo(chat)
                await borg.send_file(event.chat_id, photo)
        else:
            try:
                id = int(id)
                if id <= 0:
                    await eor(event, "رقم الهوية الذي أدخلته غير صالح")
                    return
            except BaseException:
                await eor(event, "ضع عدد جانب الامر")
                return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await borg.send_file(event.chat_id, send_photos)
            else:
                await eor(event, "ليس لديه صور 🙄")
                return