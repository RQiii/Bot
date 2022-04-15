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
def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"{full_name}"
def user_full_name(user):
    names = [user.first_name]
    names = [i for i in list(names) if i]
    return " ".join(names)
DEFAULTUSER = str(AUTONAME) if AUTONAME else str(ALIVE_NAME)
STAT_INDICATION = "**🇮🇶 ⦙   جـاري جـمـع الإحصـائيـات ، انتـظـر 🔄**"
CHANNELS_STR = "**🇮🇶 ⦙   قائمة القنوات التي أنت فيها موجودة هنا\n\n"
CHANNELS_ADMINSTR = "**🇮🇶 ⦙  قائمة القنوات التي تديرها هنا **\n\n"
CHANNELS_OWNERSTR = "**🇮🇶 ⦙  قائمة القنوات التي تمتلك فيها هنا **\n\n"
GROUPS_STR = "**🇮🇶 ⦙  قائمة المجموعات التي أنت فيها موجود هنا **\n\n"
GROUPS_ADMINSTR = "**🇮🇶 ⦙  قائمة المجموعات التي تكون مسؤولاً فيها هنا **\n\n"
GROUPS_OWNERSTR = "**🇮🇶 ⦙  قائمة المجموعات التي تمتلك فيها هنا **\n\n"
INVALID_MEDIA = "**🇮🇶 ⦙  إمتداد هذه الصورة غير صالح  ❌**"
PP_CHANGED = "**🇮🇶 ⦙  تم تغير صورة حسابك بنجاح  ✅**"
PP_TOO_SMOL = "**🇮🇶 ⦙  هذه الصورة صغيرة جدًا قم بإختيار صورة أخرى  ⚠️**"
PP_ERROR = "**🇮🇶 ⦙  حدث خطأ أثناء معالجة الصورة  ⚠️**"
BIO_SUCCESS = "**🇮🇶 ⦙  تم تغيير بايو حسابك بنجاح  ✅**"
FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
autopic_path = os.path.join(os.getcwd(), "userbot", "original_pic.png")
digitalpic_path = os.path.join(os.getcwd(), "userbot", "digital_pic.png")
autophoto_path = os.path.join(os.getcwd(), "userbot", "photo_pfp.png")
EMOJI_TELETHON = gvarstatus("ALIVE_EMOJI") or " "
OR_FOTOAUTO = gvarstatus("OR_FOTOAUTO") or "صوره وقتيه"
plagiarism = gvarstatus("OR_PLAG") or "انتحال"
unplagiarism = gvarstatus("OR_UNPLAG") or "الغاء الانتحال"
idee = gvarstatus("OR_ID") or "ايدي"
OR_NAMEAUTO = gvarstatus("OR_NAMEAUTO") or "اسم وقتي"
OR_AUTOBIO = gvarstatus("OR_AUTOBIO") or "نبذه وقتيه"
digitalpfp = gvarstatus("AUTO_PIC") or "https://telegra.ph/file/c6a84d3209402e5cd422d.mp4"
NAME_OK = "**🇮🇶 ⦙  تم تغيير اسم حسابك بنجاح  ✅**"
USERNAME_SUCCESS = "**🇮🇶 ⦙  تم تغيير معرّف حسابك بنجاح  ✅**"
USERNAME_TAKEN = "**🇮🇶 ⦙  هذا المعرّف مستخدم  ❌**"
plugin_category = "tools"
DEFAULTUSERBIO = gvarstatus("DEFAULT_BIO") or "الحمد الله"
DEFAULTUSER = AUTONAME or Config.ALIVE_NAME
LOGS = logging.getLogger(__name__)
async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE    )
    stdout, stderr = await process.communicate()
    return (        stdout.decode("utf-8", "replace").strip(),        stderr.decode("utf-8", "replace").strip(),        process.returncode,        process.pid,    )    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)
async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)
@iqthon.on(admin_cmd(pattern="احصائيات حسابي(?: |$)(.*)"))
async def stats(event):  
    cat = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            broadcast_channels += 1
            if entity.creator or entity.admin_rights:
                admin_in_broadcast_channels += 1
            if entity.creator:
                creator_in_channels += 1
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        elif not isinstance(entity, Channel) and isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"📌 **• ⚜️ |  احصائيات حسـابك العـامة لـ {full_name} 📊** \n"
    response += f"**🇮🇶 ⦙  الدردشات الخاصة 🏷️  :** {private_chats} \n"
    response += f"**🇮🇶 ⦙   الاشـخاص 🚹 : {private_chats - bots}` \n"
    response += f"**🇮🇶 ⦙   الـبوتـات 🤖 : {bots}` **\n"
    response += f"**🇮🇶 ⦙   عـدد المجـموعـات 🚻 :** `{groups}` \n"
    response += f"**🇮🇶 ⦙   عـدد القنـوات  🚻 :** `{broadcast_channels}` \n"
    response += f"**🇮🇶 ⦙   عـدد المجـموعات التـي تكـون فيها ادمـن  🛂 :** `{admin_in_groups}` \n"
    response += f"**🇮🇶 ⦙   عـدد المجموعات التـي أنـشأتـها  🛃** : `{creator_in_groups}` \n"
    response += f"**🇮🇶 ⦙   عـدد القنوات التـي تكـون فيها ادمـن 📶 : `{admin_in_broadcast_channels}` **\n"
    response += f"**🇮🇶 ⦙   حقوق المسؤول في القنوات  🛂 : `{admin_in_broadcast_channels - creator_in_channels}` **\n"
    response += f"**عـدد المحـادثـات الغيـر مقـروء 📄 :** {unread} \n"
    response += f"**عـدد الـتاكـات الغيـر مقـروء 📌 :** {unread_mentions} \n"
    response += f"**🇮🇶 ⦙   استغرق الأمر  🔍  :** `{stop_time:.02f}` ثانيه \n"
    await cat.edit(response)
    
    
    @iqthon.on(admin_cmd(pattern="قائمه (جميع القنوات|قنوات اديرها|قنوات امتلكها)$"))
async def stats(event):  
    catcmd = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    hi = []
    hica = []
    hico = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            hi.append([entity.title, entity.id])
            if entity.creator or entity.admin_rights:
                hica.append([entity.title, entity.id])
            if entity.creator:
                hico.append([entity.title, entity.id])
    if catcmd == "جميع القنوات":
        output = CHANNELS_STR
        for k, i in enumerate(hi, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_STR
    elif catcmd == "قنوات اديرها":
        output = CHANNELS_ADMINSTR
        for k, i in enumerate(hica, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_ADMINSTR
    elif catcmd == "قنوات امتلكها":
        output = CHANNELS_OWNERSTR
        for k, i in enumerate(hico, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_OWNERSTR
    stop_time = time.time() - start_time
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    output += f"\n**استغرق حساب القنوات : ** {stop_time:.02f} ثانيه"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(            catevent,
            output,
            caption=caption        )
@iqthon.on(admin_cmd(pattern="قائمه (جميع المجموعات|مجموعات اديرها|مجموعات امتلكها)$"))
async def stats(event):  
    catcmd = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    hi = []
    higa = []
    higo = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            continue
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)        ):
            hi.append([entity.title, entity.id])
            if entity.creator or entity.admin_rights:
                higa.append([entity.title, entity.id])
            if entity.creator:
                higo.append([entity.title, entity.id])
    if catcmd == "جميع المجموعات":
        output = GROUPS_STR
        for k, i in enumerate(hi, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_STR
    elif catcmd == "مجموعات اديرها":
        output = GROUPS_ADMINSTR
        for k, i in enumerate(higa, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_ADMINSTR
    elif catcmd == "مجموعات امتلكها":
        output = GROUPS_OWNERSTR
        for k, i in enumerate(higo, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_OWNERSTR
    stop_time = time.time() - start_time
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    output += f"\n**استغرق حساب المجموعات : ** {stop_time:.02f} ثانيه"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(
            catevent,
            output,
            caption=caption        )

@iqthon.on(admin_cmd(pattern="معرفاتي(?: |$)(.*)"))
async def _(event):
    result = await event.client(GetAdminedPublicChannelsRequest())
    output_str = "**🇮🇶 ⦙  جميع القنوات والمجموعات التي قمت بإنشائها  💠  :**\n"
    output_str += "".join(f"🇮🇶 ⦙    - {channel_obj.title} @{channel_obj.username} \n"
        for channel_obj in result.chats)
    await edit_or_reply(event, output_str)
@iqthon.on(admin_cmd(pattern="ملكيه ([\s\S]*)"))
async def _(event):
    user_name = event.pattern_match.group(1)
    try:
        pwd = await event.client(functions.account.GetPasswordRequest())
        my_srp_password = pwd_mod.compute_check(pwd, Config.TG_2STEP_VERIFICATION_CODE)
        await event.client(
            functions.channels.EditCreatorRequest(                channel=event.chat_id, user_id=user_name, password=my_srp_password            )        )
    except Exception as e:
        await event.edit(f"**🇮🇶 ⦙  حـدث خـطأ ✕ :**\n`{str(e)}`")
    else:
        await event.edit("**🇮🇶 ⦙  تم نقل ملكيه ✓**")
