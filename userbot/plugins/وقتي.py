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




@iqthon.iq_cmd(pattern="حفض كتابه$")
async def saf(e):
    x = await e.get_reply_message()
    if not x:
        return await eod(            e, "قم بالرد على أي رسالة لحفظها في رسائلك المحفوظة", time=5        )
    if e.out:
        await e.client.send_message("me", x)
    else:
        await e.client.send_message(e.sender_id, x)
    await eor(e, "تم حفظ الرسالة", time=5)

@iqthon.iq_cmd(pattern="حفض توجيه$")
async def saf(e):
    x = await e.get_reply_message()
    if not x:
        return await eod(            e, "قم بالرد على أي رسالة لحفظها في رسائلك المحفوظة", time=5        )
    if e.out:
        await x.forward_to("me")
    else:
        await x.forward_to(e.sender_id)
    await eor(e, "تم حفظ الرسالة.", time=5)

@iqthon.on(admin_cmd(pattern="وضع بايو(?: |$)(.*)"))
async def _(event):
    bio = event.pattern_match.group(1)
    try:
        await event.client(functions.account.UpdateProfileRequest(about=bio))
        await edit_delete(event, "**🇮🇶 ⦙  تم تغيير البايو بنجاح  ✅**")
    except Exception as e:
        await edit_or_reply(event, f"**🇮🇶 ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
@iqthon.on(admin_cmd(pattern="وضع اسم(?: |$)(.*)"))
async def _(event):
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if ";" in names:
        first_name, last_name = names.split("|", 1)
    try:
        await event.client(
            functions.account.UpdateProfileRequest(                first_name=first_name, last_name=last_name            )        )
        await edit_delete(event, "**🇮🇶 ⦙  تم تغيير الاسم بنجاح  ✅**")
    except Exception as e:
        await edit_or_reply(event, f"**🇮🇶 ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
@iqthon.on(admin_cmd(pattern="وضع صوره(?: |$)(.*)"))
async def _(event):
    reply_message = await event.get_reply_message()
    catevent = await edit_or_reply(        event, "**...**"    )
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    photo = None
    try:
        photo = await event.client.download_media(            reply_message, Config.TMP_DOWNLOAD_DIRECTORY        )
    except Exception as e:
        await catevent.edit(str(e))
    else:
        if photo:
            await catevent.edit("**🇮🇶 ⦙   أشترك @pmmvn**")
            if photo.endswith((".mp4", ".MP4")):
                # https://t.me/tgbetachat/324694
                size = os.stat(photo).st_size
                if size > 2097152:
                    await catevent.edit("**🇮🇶 ⦙   يجب ان يكون الحجم اقل من 2 ميغا ✅**")
                    os.remove(photo)
                    return
                catpic = None
                catvideo = await event.client.upload_file(photo)
            else:
                catpic = await event.client.upload_file(photo)
                catvideo = None
            try:
                await event.client(
                    functions.photos.UploadProfilePhotoRequest(                        file=catpic, video=catvideo, video_start_ts=0.01                   )                )
            except Exception as e:
                await catevent.edit(f"**🇮🇶 ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
            else:
                await edit_or_reply(                    catevent, "**🇮🇶 ⦙   تم تغيير الصورة بنجاح ✅**"                )
    try:
        os.remove(photo)
    except Exception as e:
        LOGS.info(str(e))
async def digitalpicloop():
    DIGITALPICSTART = gvarstatus("صوره وقتيه") == "true"
    i = 0
    while DIGITALPICSTART:
        if not os.path.exists(digitalpic_path):
            downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        shutil.copy(digitalpic_path, autophoto_path)
        Image.open(autophoto_path)
        current_time = datetime.now().strftime("%I:%M")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        cat = str(base64.b64decode("dXNlcmJvdC9zcWxfaGVscGVyL0lRVEhPTklNT0dFLnR0Zg=="))[            2:36        ]
        fnt = ImageFont.truetype(cat, 65)
        drawn_text.text((300, 400), current_time, font=fnt, fill=(255, 255, 255))
        img.save(autophoto_path)
        file = await iqthon.upload_file(autophoto_path)
        try:
            if i > 0:
                await iqthon(                    functions.photos.DeletePhotosRequest(                        await iqthon.get_profile_photos("me", limit=1)                   )                )
            i += 1
            await iqthon(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(autophoto_path)
            await asyncio.sleep(60)
        except BaseException:
            return
        DIGITALPICSTART = gvarstatus("صوره وقتيه") == "true"


@iqthon.on(admin_cmd(pattern=f"{OR_FOTOAUTO}(?: |$)(.*)"))
async def _(event):
    downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
    downloader.start(blocking=False)
    while not downloader.isFinished():
        pass
    if gvarstatus(f"{OR_FOTOAUTO}") is not None and gvarstatus(f"{OR_FOTOAUTO}") == "true":
        return await edit_delete(event, f"**🇮🇶 ⦙  صوره وقتيه مفعّلـة بالفعـل !**")
    addgvar(f"{OR_FOTOAUTO}", True)
    await edit_delete(event, f"**🇮🇶 ⦙  تـمّ بـدأ الصـورة الديجيتـال بواسطـة المستخـدم ✓**")
    await digitalpicloop()
@iqthon.on(admin_cmd(pattern="نبهثهبهخقخلم ?(.*)"))
async def _(e):
    files = e.pattern_match.group(1)
    if not files:
        files = "*"
    elif files.endswith("/"):
        files = files + "*"
    elif "*" not in files:
        files = files + "/*"
    files = glob.glob(files)
    if not files:
        return await eor(e, "الدليل فارغ أو غير صحيح", time=5)
    pyfiles = []
    jsons = []
    vdos = []
    audios = []
    pics = []
    others = []
    otherfiles = []
    folders = []
    text = []
    apk = []
    exe = []
    zip_ = []
    book = []
    for file in sorted(files):
        if os.path.isdir(file):
            folders.append("📂 " + str(file))
        elif str(file).endswith(".py"):
            pyfiles.append("🐍 " + str(file))
        elif str(file).endswith(".json"):
            jsons.append("🔮 " + str(file))
        elif str(file).endswith((".mkv", ".mp4", ".avi", ".gif", "webm")):
            vdos.append("🎥 " + str(file))
        elif str(file).endswith((".mp3", ".ogg", ".m4a", ".opus")):
            audios.append("🔊 " + str(file))
        elif str(file).endswith((".jpg", ".jpeg", ".png", ".webp")):
            pics.append("🖼 " + str(file))
        elif str(file).endswith((".txt", ".text", ".log")):
            text.append("📄 " + str(file))
        elif str(file).endswith((".apk", ".xapk")):
            apk.append("📲 " + str(file))
        elif str(file).endswith(".exe"):
            exe.append("⚙ " + str(file))
        elif str(file).endswith((".zip", ".rar")):
            zip_.append("🗜 " + str(file))
        elif str(file).endswith((".pdf", ".epub")):
            book.append("📗 " + str(file))
        elif "." in str(file)[1:]:
            others.append("🏷 " + str(file))
        else:
            otherfiles.append("📒 " + str(file))
    omk = [        *sorted(folders),        *sorted(pyfiles),        *sorted(jsons),        *sorted(zip_),        *sorted(vdos),        *sorted(pics),        *sorted(audios),        *sorted(apk),        *sorted(exe),        *sorted(book),        *sorted(text),        *sorted(others),        *sorted(otherfiles),    ]
    text = ""
    fls, fos = 0, 0
    flc, foc = 0, 0
    for i in omk:
        try:
            emoji = i.split()[0]
            name = i.split(maxsplit=1)[1]
            nam = name.split("/")[-1]
            if os.path.isdir(name):
                size = 0
                for path, dirs, files in os.walk(name):
                    for f in files:
                        fp = os.path.join(path, f)
                        size += os.path.getsize(fp)
                if hb(size):
                    text += emoji + f" `{nam}`" + "  `" + hb(size) + "`\n"
                    fos += size
                else:
                    text += emoji + f" `{nam}`" + "\n"
                foc += 1
            else:
                if hb(int(os.path.getsize(name))):
                    text += (                        emoji                        + f" `{nam}`"                        + "  `"                        + hb(int(os.path.getsize(name)))                        + "`\n"                    )
                    fls += int(os.path.getsize(name))
                else:
                    text += emoji + f" `{nam}`" + "\n"
                flc += 1
        except BaseException:
            pass
    tfos, tfls, ttol = hb(fos), hb(fls), hb(fos + fls)
    if not hb(fos):
        tfos = "0 B"
    if not hb(fls):
        tfls = "0 B"
    if not hb(fos + fls):
        ttol = "0 B"
    text += f"\n\nالمجلدات :  `{foc}` :   `{tfos}`\nعدد الملفات :       `{flc}` :   `{tfls}`\nالمجموع :       `{flc+foc}` :   `{ttol}`"
    try:
        await eor(e, text)
    except MessageTooLongError:
        with io.BytesIO(str.encode(text)) as out_file:
            out_file.name = "output.txt"
            await e.reply(                f"`{e.text}`", file=out_file, thumb=None ) 
        await e.delete()
@iqthon.on(admin_cmd(pattern="كول (.*)"))
async def _(event):
    bxt = Config.TG_BOT_USERNAME
    try:
        tex = str(event.text[6:])
        await tgbot.send_message(event.chat_id, tex)
        await event.delete()
    except BaseException:
        await event.client.send_message(event.chat_id, f"رجاء اضف البوت الخاص بك هنا : @{bxt}  !")
        await event.delete()
def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = int(len(line) / 55)
                for z in range(1, k + 2):
                    lines.append(line[((z - 1) * 55) : (z * 55)])
    return lines[:25]
    

@iqthon.on(admin_cmd(pattern="كتابه ?(.*)"))
async def writer(e):
    if e.reply_to:
        reply = await e.get_reply_message()
        text = reply.message
    elif e.pattern_match.group(1):
        text = e.text.split(maxsplit=1)[1]
    else:
        return await e.edit("Privode Some Text🥲")
    img = Image.open("SQL/template.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("SQL/assfont.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    line_height = font.getsize("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "iqthon_Write.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)
    await e.delete()
@iqthon.on(admin_cmd(pattern="عد الردود ?(.*)"))
async def _(event):
    await eor(event, "جاري العد ...")
    count = -1
    message = event.message
    while message:
        reply = await message.get_reply_message()
        if reply is None:
            await borg(                SaveDraftRequest(                    await event.get_input_chat(), "", reply_to_msg_id=message.id                )            )
        message = reply
        count += 1
    await eor(event, f"عدد الردود على هذا الرساله : {count}")

@iqthon.on(admin_cmd(pattern="زاجل ?(.*)"))
async def pmto(event):
    a = event.pattern_match.group(1)
    b = a.split(" ")
    chat_id = b[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    msg = ""
    for i in b[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await borg.send_message(chat_id, msg)
        await event.edit("تم الارسال !🤗")
    except BaseException:
        await event.edit("هناك خطا .")
@iqthon.on(admin_cmd(pattern=f"{OR_NAMEAUTO}(?: |$)(.*)"))
async def _(event):
    if gvarstatus(f"{OR_NAMEAUTO}") is not None and gvarstatus(f"{OR_NAMEAUTO}") == "true":
        return await edit_delete(event, f"**🇮🇶 ⦙  الإسـم الوقتـي قيـد التشغيـل بالفعـل !**")
    addgvar(f"{OR_NAMEAUTO}", True)
    await edit_delete(event, "**🇮🇶 ⦙  تـمّ بـدأ الإسـم الوقتـي بواسطـة المستخـدم ✓**")
    await autoname_loop()
@iqthon.on(admin_cmd(pattern=f"{OR_AUTOBIO}(?: |$)(.*)"))
async def _(event):
    "🇮🇶 ⦙  يحـدّث البايـو مع الوقـت 💡"
    if gvarstatus(f"{OR_AUTOBIO}") is not None and gvarstatus(f"{OR_AUTOBIO}") == "true":
        return await edit_delete(event, f"**🇮🇶 ⦙  البايـو الوقتـي قيـد التشغيـل بالفعـل !**")
    addgvar(f"{OR_AUTOBIO}", True)
    await edit_delete(event, "**🇮🇶 ⦙  تـمّ بـدأ البايـو الوقتـي بواسطـة المستخـدم ✓**")
    await autobio_loop()
@iqthon.iq_cmd(pattern="سمول(?: |$)(.*)")
async def ultiny(event):
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await event.edit("قم بالرد على صوره او ملصق لتصغيره")
        return
    xx = await event.edit("جاري التصغير ...")
    ik = await event.client.download_media(reply)
    im1 = Image.open("SQL/blank.png")
    if ik.endswith(".tgs"):
        await event.client.download_media(reply, "ult.tgs")
        await bash("lottie_convert.py ult.tgs json.json")
        with open("json.json") as json:
            jsn = json.read()
        jsn = jsn.replace("512", "2000")
        open("json.json", "w").write(jsn)
        await bash("lottie_convert.py json.json ult.tgs")
        file = "ult.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        dani, busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await event.client.send_file(event.chat_id, file, reply_to=event.reply_to_msg_id)
    await xx.delete()
    os.remove(file)
    os.remove(ik)

@iqthon.on(admin_cmd(pattern="انمي_تلقائي ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./DOWNLOADS/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(            "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n                                                   Time: %I:%M:%S \n                                                   Date: %d/%m/%y "        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((300, 450), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo)
        file = await event.client.upload_file(photo)  
        try:
            await event.client(                functions.photos.UploadProfilePhotoRequest(file)  )
            os.remove(photo)

            await asyncio.sleep(60)
        except:
            return
@iqthon.on(admin_cmd(pattern="ايقاف ([\s\S]*)"))
async def _(event):  # sourcery no-metrics
    input_str = event.pattern_match.group(1)
    if input_str == f"{OR_FOTOAUTO}":
        if gvarstatus(f"{OR_FOTOAUTO}") is not None and gvarstatus(f"{OR_FOTOAUTO}") == "true":
            delgvar(f"{OR_FOTOAUTO}")
            await event.client(
                functions.photos.DeletePhotosRequest(                    await event.client.get_profile_photos("me", limit=1)                )            )
            return await edit_delete(event, "**🇮🇶 ⦙  تم إيقـاف  صوره وقتيه الآن ✓**")
        return await edit_delete(event, "**🇮🇶 ⦙  لم يتـم تفعيـل صوره وقتيه ✕**")
    if input_str == f"{OR_NAMEAUTO}":
        if gvarstatus(f"{OR_NAMEAUTO}") is not None and gvarstatus(f"{OR_NAMEAUTO}") == "true":
            delgvar(f"{OR_NAMEAUTO}")
            await event.client(                functions.account.UpdateProfileRequest(first_name=DEFAULTUSER)            )
            return await edit_delete(event, "**🇮🇶 ⦙  تم إيقـاف الإسـم الوقتـي الآن ✓**")
        return await edit_delete(event, "**🇮🇶 ⦙  لم يتـم تفعيـل الإسـم الوقتـي ✕**")
    if input_str == f"{OR_AUTOBIO}":
        if gvarstatus(f"{OR_AUTOBIO}") is not None and gvarstatus(f"{OR_AUTOBIO}") == "true":
            delgvar(f"{OR_AUTOBIO}")
            await event.client(                functions.account.UpdateProfileRequest(about=DEFAULTUSERBIO)            )
            return await edit_delete(event, "**🇮🇶 ⦙  تم إيقـاف البايـو التلقائـي الآن ✓**")
        return await edit_delete(event, "**🇮🇶 ⦙  لم يتـم تفعيـل البايـو التلقائـي ✕**")
    END_CMDS = [f"{OR_FOTOAUTO}", f"{OR_NAMEAUTO}", f"{OR_AUTOBIO}",]
    if input_str not in END_CMDS:
        await edit_delete(            event,            f"🇮🇶 ⦙   {input_str} أمـر الإنهـاء غيـر صالـح، اذڪـر بوضـوح ما يجـب أن أنهـي !",            parse_mode=_format.parse_pre        )
iqthon.loop.create_task(digitalpicloop())
iqthon.loop.create_task(autoname_loop())
iqthon.loop.create_task(autobio_loop())
